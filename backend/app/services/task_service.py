from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task
from app.models.task_enums import TaskPriority, TaskStatus
from app.repositories.category_repository import CategoryRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.tag_repository import TagRepository
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.exceptions import NotFoundError, ValidationError


class TaskService:
    """Business rules and operations for tasks."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

        self.task_repository = TaskRepository(session)
        self.project_repository = ProjectRepository(session)
        self.category_repository = CategoryRepository(session)
        self.tag_repository = TagRepository(session)

    async def _validate_project(
        self,
        project_id: UUID | None,
        user_id: UUID,
    ) -> None:
        """Ensure an assigned project belongs to the authenticated user."""
        if project_id is None:
            return

        project = await self.project_repository.get_by_id_and_user(
            project_id,
            user_id,
        )

        if project is None:
            raise ValidationError("Project not found or does not belong to you")

    async def _validate_category(
        self,
        category_id: UUID | None,
        user_id: UUID,
    ) -> None:
        """Ensure an assigned category belongs to the authenticated user."""
        if category_id is None:
            return

        category = await self.category_repository.get_by_id_and_user(
            category_id,
            user_id,
        )

        if category is None:
            raise ValidationError("Category not found or does not belong to you")

    async def _get_valid_tags(
        self,
        tag_ids: list[UUID],
        user_id: UUID,
    ) -> list[Tag]:
        """Return tags only when every supplied tag belongs to the user."""
        unique_tag_ids = list(set(tag_ids))

        tags = await self.tag_repository.get_many_by_ids_and_user(
            unique_tag_ids,
            user_id,
        )

        if len(tags) != len(unique_tag_ids):
            raise ValidationError(
                "One or more tags were not found or do not belong to you"
            )

        return tags

    async def _validate_parent_task(
        self,
        parent_task_id: UUID | None,
        user_id: UUID,
        *,
        task_id: UUID | None = None,
    ) -> None:
        """Ensure the parent task exists, belongs to the user, and is not self."""
        if parent_task_id is None:
            return

        if task_id is not None and parent_task_id == task_id:
            raise ValidationError("A task cannot be its own parent")

        parent_task = await self.task_repository.get_by_id_and_user(
            parent_task_id,
            user_id,
        )

        if parent_task is None:
            raise ValidationError(
                "Parent task not found or does not belong to you"
            )

    async def create_task(
        self,
        user_id: UUID,
        data: TaskCreate,
    ) -> Task:
        """Create a task after validating all related resources."""
        await self._validate_project(data.project_id, user_id)
        await self._validate_category(data.category_id, user_id)
        await self._validate_parent_task(data.parent_task_id, user_id)

        tags = await self._get_valid_tags(data.tag_ids, user_id)

        task_data = data.model_dump(exclude={"tag_ids"})

        if task_data["status"] == TaskStatus.COMPLETED:
            task_data["completed_at"] = datetime.now(timezone.utc)

        task = await self.task_repository.create(
            data={
                **task_data,
                "user_id": user_id,
            }
        )

        task.tags = tags

        await self.session.commit()
        await self.session.refresh(task)

        return task

    async def get_task(
        self,
        user_id: UUID,
        *,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: UUID | None = None,
        category_id: UUID | None = None,
        due_before: datetime | None = None,
        due_after: datetime | None = None,
        include_completed: bool = True,
        offset: int = 0,
        limit: int = 100,
    ) -> Task:
        """Get one task owned by the authenticated user."""
        task = await self.task_repository.get_by_id_and_user(
            task_id,
            user_id,
        )

        if task is None:
            raise NotFoundError("Task not found")

        return task

    async def get_tasks(
        self,
        user_id: UUID,
        *,
        status: TaskStatus | None = None,
        priority=None,
        project_id: UUID | None = None,
        category_id: UUID | None = None,
        due_before: datetime | None = None,
        due_after: datetime | None = None,
        include_completed: bool = True,
        offset: int = 0,
        limit: int = 100,
    ):
        """Get filtered tasks for the authenticated user."""
        return await self.task_repository.get_all_by_user(
            user_id,
            status=status,
            priority=priority,
            project_id=project_id,
            category_id=category_id,
            due_before=due_before,
            due_after=due_after,
            include_completed=include_completed,
            offset=offset,
            limit=limit,
        )

    async def update_task(
        self,
        task_id: UUID,
        user_id: UUID,
        data: TaskUpdate,
    ) -> Task:
        """Update a task while enforcing relationship and status rules."""
        task = await self.get_task(task_id, user_id)

        update_data = data.model_dump(exclude_unset=True)

        if not update_data:
            return task

        if "project_id" in update_data:
            await self._validate_project(update_data["project_id"], user_id)

        if "category_id" in update_data:
            await self._validate_category(update_data["category_id"], user_id)

        if "parent_task_id" in update_data:
            await self._validate_parent_task(
                update_data["parent_task_id"],
                user_id,
                task_id=task.id,
            )

        if "tag_ids" in update_data:
            tag_ids = update_data.pop("tag_ids")

            if tag_ids is not None:
                task.tags = await self._get_valid_tags(tag_ids, user_id)

        if "status" in update_data:
            new_status = update_data["status"]

            if (
                new_status == TaskStatus.COMPLETED
                and task.status != TaskStatus.COMPLETED
            ):
                update_data["completed_at"] = datetime.now(timezone.utc)

            elif (
                new_status != TaskStatus.COMPLETED
                and task.status == TaskStatus.COMPLETED
            ):
                update_data["completed_at"] = None

        task = await self.task_repository.update(task, data=update_data)

        await self.session.commit()
        await self.session.refresh(task)

        return task

    async def delete_task(
        self,
        task_id: UUID,
        user_id: UUID,
    ) -> None:
        """Soft-delete a task owned by the authenticated user."""
        task = await self.get_task(task_id, user_id)

        await self.task_repository.soft_delete(task)
        await self.session.commit()

    async def get_subtasks(
        self,
        task_id: UUID,
        user_id: UUID,
    ):
        """Get subtasks after confirming the parent task belongs to the user."""
        await self.get_task(task_id, user_id)

        return await self.task_repository.get_subtasks(task_id, user_id)