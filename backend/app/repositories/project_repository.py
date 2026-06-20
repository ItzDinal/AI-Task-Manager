from uuid import UUID

from sqlalchemy import func,select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import Project
from app.repositories.base import BaseRepository


class ProjectRepository(BaseRepository[Project]):
    """Database operations specific to projects."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Project)

    async def get_by_id_and_user(
        self,
        project_id: UUID,
        user_id: UUID,
    ) -> Project | None:
        """Return one active project only if it belongs to the user."""
        statement = (
            self._base_query()
            .where(Project.id == project_id)
            .where(Project.user_id == user_id)
        )

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_all_by_user(
        self,
        user_id: UUID,
        *,
        include_archived: bool = False,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Project]:
        """Return a user's projects, newest first."""
        statement = (
            self._base_query()
            .where(Project.user_id == user_id)
        )

        if not include_archived:
            statement = statement.where(Project.is_archived.is_(False))

        statement = (
            statement
            .order_by(Project.created_at.desc())
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def count_by_user(
        self,
        user_id: UUID,
        *,
        include_archived: bool = False,
    ) -> int:
        """Count a user's active projects."""
        statement = (
            select(Project)
            .where(Project.user_id == user_id)
            .where(Project.is_deleted.is_(False))
        )

        if not include_archived:
            statement = statement.where(Project.is_archived.is_(False))

        result = await self.session.execute(statement)
        return len(result.scalars().all())