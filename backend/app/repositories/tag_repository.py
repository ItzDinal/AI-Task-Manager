from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tag import Tag
from app.repositories.base import BaseRepository


class TagRepository(BaseRepository[Tag]):
    """Database operations specific to tags."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Tag)

    async def get_by_id_and_user(
        self,
        tag_id: UUID,
        user_id: UUID,
    ) -> Tag | None:
        """Return one active tag only if it belongs to the user."""
        statement = (
            self._base_query()
            .where(Tag.id == tag_id)
            .where(Tag.user_id == user_id)
        )

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_by_name_and_user(
        self,
        name: str,
        user_id: UUID,
    ) -> Tag | None:
        """Find an active tag by name for one user."""
        statement = (
            self._base_query()
            .where(Tag.user_id == user_id)
            .where(func.lower(Tag.name) == name.strip().lower())
        )

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_many_by_ids_and_user(
        self,
        tag_ids: list[UUID],
        user_id: UUID,
    ) -> list[Tag]:
        """
        Return active tags belonging to this user for the supplied IDs.

        The service layer will compare the returned count with the requested
        count to detect invalid tag IDs or tags owned by another user.
        """
        if not tag_ids:
            return []

        statement = (
            self._base_query()
            .where(Tag.user_id == user_id)
            .where(Tag.id.in_(tag_ids))
            .order_by(Tag.name.asc())
        )

        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def get_all_by_user(
        self,
        user_id: UUID,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Tag]:
        """Return a user's active tags alphabetically."""
        statement = (
            self._base_query()
            .where(Tag.user_id == user_id)
            .order_by(Tag.name.asc())
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def count_by_user(self, user_id: UUID) -> int:
        """Count a user's active tags."""
        statement = (
            select(func.count())
            .select_from(Tag)
            .where(Tag.user_id == user_id)
            .where(Tag.is_deleted.is_(False))
        )

        result = await self.session.execute(statement)
        return result.scalar_one()