from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    """Database operations specific to categories."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Category)

    async def get_by_id_and_user(
        self,
        category_id: UUID,
        user_id: UUID,
    ) -> Category | None:
        """Return one active category only if it belongs to the user."""
        statement = (
            self._base_query()
            .where(Category.id == category_id)
            .where(Category.user_id == user_id)
        )

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_by_name_and_user(
        self,
        name: str,
        user_id: UUID,
    ) -> Category | None:
        """
        Find an active category by name for one user.

        This lets the service prevent duplicate category names per user.
        """
        statement = (
            self._base_query()
            .where(Category.user_id == user_id)
            .where(func.lower(Category.name) == name.strip().lower())
        )

        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def get_all_by_user(
        self,
        user_id: UUID,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Category]:
        """Return a user's active categories alphabetically."""
        statement = (
            self._base_query()
            .where(Category.user_id == user_id)
            .order_by(Category.name.asc())
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(statement)
        return list(result.scalars().all())

    async def count_by_user(self, user_id: UUID) -> int:
        """Count a user's active categories."""
        statement = (
            select(func.count())
            .select_from(Category)
            .where(Category.user_id == user_id)
            .where(Category.is_deleted.is_(False))
        )

        result = await self.session.execute(statement)
        return result.scalar_one()