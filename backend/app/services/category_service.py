from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.services.exceptions import ConflictError, NotFoundError


class CategoryService:
    """Business rules and operations for categories."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.repository = CategoryRepository(session)

    async def create_category(
        self,
        user_id: UUID,
        data: CategoryCreate,
    ) -> Category:
        """Create a category, preventing duplicate names per user."""
        existing_category = await self.repository.get_by_name_and_user(
            data.name,
            user_id,
        )

        if existing_category is not None:
            raise ConflictError("A category with this name already exists")

        category = await self.repository.create(
            data={
                **data.model_dump(),
                "user_id": user_id,
            }
        )

        await self.session.commit()
        await self.session.refresh(category)

        return category

    async def get_category(
        self,
        category_id: UUID,
        user_id: UUID,
    ) -> Category:
        """Get one active category owned by the user."""
        category = await self.repository.get_by_id_and_user(
            category_id,
            user_id,
        )

        if category is None:
            raise NotFoundError("Category not found")

        return category

    async def get_categories(
        self,
        user_id: UUID,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Category]:
        """Get active categories for a user."""
        return await self.repository.get_all_by_user(
            user_id,
            offset=offset,
            limit=limit,
        )

    async def update_category(
        self,
        category_id: UUID,
        user_id: UUID,
        data: CategoryUpdate,
    ) -> Category:
        """Update a category and prevent duplicate names."""
        category = await self.get_category(category_id, user_id)

        update_data = data.model_dump(exclude_unset=True)

        if not update_data:
            return category

        new_name = update_data.get("name")

        if new_name is not None and new_name.lower() != category.name.lower():
            existing_category = await self.repository.get_by_name_and_user(
                new_name,
                user_id,
            )

            if (
                existing_category is not None
                and existing_category.id != category.id
            ):
                raise ConflictError("A category with this name already exists")

        category = await self.repository.update(
            category,
            data=update_data,
        )

        await self.session.commit()
        await self.session.refresh(category)

        return category

    async def delete_category(
        self,
        category_id: UUID,
        user_id: UUID,
    ) -> None:
        """Soft-delete a category owned by the user."""
        category = await self.get_category(category_id, user_id)

        await self.repository.soft_delete(category)
        await self.session.commit()

    async def restore_category(
        self,
        category_id: UUID,
        user_id: UUID,
    ) -> Category:
        """Restore a soft-deleted category owned by the user."""
        result = await self.session.execute(
            select(Category).where(
                Category.id == category_id,
                Category.user_id == user_id,
                Category.is_deleted.is_(True),
            )
        )
        category = result.scalar_one_or_none()

        if category is None:
            raise NotFoundError("Deleted category not found")

        # Prevent restore if an active category now uses the same name.
        existing_category = await self.repository.get_by_name_and_user(
            category.name,
            user_id,
        )
        if existing_category is not None:
            raise ConflictError(
                "Cannot restore category because that name is already in use"
            )

        category = await self.repository.restore(category)

        await self.session.commit()
        await self.session.refresh(category)

        return category