from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.services.exceptions import ConflictError, NotFoundError


class ProjectService:
    """Business rules and operations for projects."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.repository = ProjectRepository(session)

    async def create_project(
        self,
        user_id: UUID,
        data: ProjectCreate,
    ) -> Project:
        """Create a project for the authenticated user."""
        project = await self.repository.create(
            data={
                **data.model_dump(),
                "user_id": user_id,
            }
        )

        await self.session.commit()
        await self.session.refresh(project)

        return project

    async def get_project(
        self,
        project_id: UUID,
        user_id: UUID,
    ) -> Project:
        """Get one project owned by the user."""
        project = await self.repository.get_by_id_and_user(
            project_id,
            user_id,
        )

        if project is None:
            raise NotFoundError("Project not found")

        return project

    async def get_projects(
        self,
        user_id: UUID,
        *,
        include_archived: bool = False,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Project]:
        """Get the user's projects."""
        return await self.repository.get_all_by_user(
            user_id,
            include_archived=include_archived,
            offset=offset,
            limit=limit,
        )

    async def update_project(
        self,
        project_id: UUID,
        user_id: UUID,
        data: ProjectUpdate,
    ) -> Project:
        """Update a project owned by the user."""
        project = await self.get_project(project_id, user_id)

        update_data = data.model_dump(exclude_unset=True)

        if not update_data:
            return project

        project = await self.repository.update(
            project,
            data=update_data,
        )

        await self.session.commit()
        await self.session.refresh(project)

        return project

    async def delete_project(
        self,
        project_id: UUID,
        user_id: UUID,
    ) -> None:
        """Soft-delete a project owned by the user."""
        project = await self.get_project(project_id, user_id)

        await self.repository.soft_delete(project)
        await self.session.commit()

    async def restore_project(
        self,
        project_id: UUID,
        user_id: UUID,
    ) -> Project:
        """
        Restore a soft-deleted project.

        We query directly because the normal repository query intentionally
        hides soft-deleted records.
        """
        from sqlalchemy import select

        result = await self.session.execute(
            select(Project).where(
                Project.id == project_id,
                Project.user_id == user_id,
                Project.is_deleted.is_(True),
            )
        )
        project = result.scalar_one_or_none()

        if project is None:
            raise NotFoundError("Deleted project not found")

        project = await self.repository.restore(project)

        await self.session.commit()
        await self.session.refresh(project)

        return project