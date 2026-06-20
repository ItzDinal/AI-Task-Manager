from __future__ import annotations

from datetime import datetime
from typing import Sequence
from uuid import UUID

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.task import Task
from app.models.task_enums import TaskPriority, TaskStatus
from app.repositories.base import BaseRepository


class TaskRepository(BaseRepository[Task]):
    """Database operations specific to tasks."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Task)

    def _task_query(self) -> Select[tuple[Task]]:
        """
        Base task query with relationships needed in API responses.

        selectinload avoids an N+1 query problem when returning many tasks.
        """
        return (
            select(Task)
            .options(
                selectinload(Task.tags),
                selectinload(Task.project),
                selectinload(Task.category),
                selectinload(Task.subtasks),
            )
            .where(Task.is_deleted.is_(False))
        )

    async def get_by_id_and_user(
        self,
        task_id: UUID,
        user_id: UUID,
    ) -> Task | None:
        """Return one active task only if it belongs to the user."""
        statement = (
            self._task_query()
            .where(Task.id == task_id)
            .where(Task.user_id == user_id)
        )

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_all_by_user(
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
    ) -> Sequence[Task]:
        """
        Return filtered tasks for one user.

        `status` and `priority` are strings here intentionally. The service
        layer will validate API input using TaskStatus and TaskPriority.
        """
        statement = self._task_query().where(Task.user_id == user_id)

        if status is not None:
            statement = statement.where(Task.status == status)

        if priority is not None:
            statement = statement.where(Task.priority == priority)

        if project_id is not None:
            statement = statement.where(Task.project_id == project_id)

        if category_id is not None:
            statement = statement.where(Task.category_id == category_id)

        if due_before is not None:
            statement = statement.where(Task.due_date <= due_before)

        if due_after is not None:
            statement = statement.where(Task.due_date >= due_after)

        if not include_completed:
            statement = statement.where(
                Task.status != TaskStatus.COMPLETED
            )

        statement = (
            statement
            .order_by(Task.position.asc(), Task.created_at.desc())
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(statement)
        return result.scalars().unique().all()

    async def count_by_user(
        self,
        user_id: UUID,
        *,
        status: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: UUID | None = None,
        category_id: UUID | None = None,
        include_completed: bool = True,
    ) -> int:
        """Count tasks for pagination using the same common filters."""
        statement = (
            select(func.count())
            .select_from(Task)
            .where(Task.user_id == user_id)
            .where(Task.is_deleted.is_(False))
        )

        if status is not None:
            statement = statement.where(Task.status == status)

        if priority is not None:
            statement = statement.where(Task.priority == priority)

        if project_id is not None:
            statement = statement.where(Task.project_id == project_id)

        if category_id is not None:
            statement = statement.where(Task.category_id == category_id)

        if not include_completed:
            statement = statement.where(Task.status != TaskStatus.COMPLETED)

        result = await self.session.execute(statement)
        return result.scalar_one()

    async def get_subtasks(
        self,
        parent_task_id: UUID,
        user_id: UUID,
    ) -> Sequence[Task]:
        """Return active subtasks for a parent task owned by the user."""
        statement = (
            self._task_query()
            .where(Task.parent_task_id == parent_task_id)
            .where(Task.user_id == user_id)
            .order_by(Task.position.asc(), Task.created_at.asc())
        )

        result = await self.session.execute(statement)
        return result.scalars().unique().all()