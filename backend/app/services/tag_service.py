from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tag import Tag
from app.repositories.tag_repository import TagRepository
from app.schemas.tag import TagCreate, TagUpdate
from app.services.exceptions import ConflictError, NotFoundError


class TagService:
    """Business rules and operations for tags."""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.repository = TagRepository(session)

    async def create_tag(
        self,
        user_id: UUID,
        data: TagCreate,
    ) -> Tag:
        """Create a tag, preventing duplicate names per user."""
        existing_tag = await self.repository.get_by_name_and_user(
            data.name,
            user_id,
        )

        if existing_tag is not None:
            raise ConflictError("A tag with this name already exists")

        tag = await self.repository.create(
            data={
                **data.model_dump(),
                "user_id": user_id,
            }
        )

        await self.session.commit()
        await self.session.refresh(tag)

        return tag

    async def get_tag(
        self,
        tag_id: UUID,
        user_id: UUID,
    ) -> Tag:
        """Get one active tag owned by the user."""
        tag = await self.repository.get_by_id_and_user(tag_id, user_id)

        if tag is None:
            raise NotFoundError("Tag not found")

        return tag

    async def get_tags(
        self,
        user_id: UUID,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Tag]:
        """Get active tags for a user."""
        return await self.repository.get_all_by_user(
            user_id,
            offset=offset,
            limit=limit,
        )

    async def update_tag(
        self,
        tag_id: UUID,
        user_id: UUID,
        data: TagUpdate,
    ) -> Tag:
        """Update a tag and prevent duplicate names."""
        tag = await self.get_tag(tag_id, user_id)

        update_data = data.model_dump(exclude_unset=True)

        if not update_data:
            return tag

        new_name = update_data.get("name")

        if new_name is not None and new_name.lower() != tag.name.lower():
            existing_tag = await self.repository.get_by_name_and_user(
                new_name,
                user_id,
            )

            if existing_tag is not None and existing_tag.id != tag.id:
                raise ConflictError("A tag with this name already exists")

        tag = await self.repository.update(tag, data=update_data)

        await self.session.commit()
        await self.session.refresh(tag)

        return tag

    async def delete_tag(
        self,
        tag_id: UUID,
        user_id: UUID,
    ) -> None:
        """Soft-delete a tag owned by the user."""
        tag = await self.get_tag(tag_id, user_id)

        await self.repository.soft_delete(tag)
        await self.session.commit()

    async def restore_tag(
        self,
        tag_id: UUID,
        user_id: UUID,
    ) -> Tag:
        """Restore a soft-deleted tag owned by the user."""
        result = await self.session.execute(
            select(Tag).where(
                Tag.id == tag_id,
                Tag.user_id == user_id,
                Tag.is_deleted.is_(True),
            )
        )
        tag = result.scalar_one_or_none()

        if tag is None:
            raise NotFoundError("Deleted tag not found")

        existing_tag = await self.repository.get_by_name_and_user(
            tag.name,
            user_id,
        )

        if existing_tag is not None:
            raise ConflictError(
                "Cannot restore tag because that name is already in use"
            )

        tag = await self.repository.restore(tag)

        await self.session.commit()
        await self.session.refresh(tag)

        return tag