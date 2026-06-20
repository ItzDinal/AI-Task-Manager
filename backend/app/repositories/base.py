from __future__ import annotations

from typing import Any, Generic, Sequence, TypeVar
from uuid import UUID
from datetime import datetime, timezone

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class BaseRepository(Generic[ModelType]):
    """
    Reusable async CRUD repository.

    Child repositories provide the SQLAlchemy model class:
        super().__init__(session, Project)
    """

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ) -> None:
        self.session = session
        self.model = model

    def _base_query(self) -> Select[tuple[ModelType]]:
        """
        Base query for active records only.

        All Phase 2 models use SoftDeleteMixin, so they have is_deleted.
        """
        return select(self.model).where(self.model.is_deleted.is_(False))

    async def get_by_id(self, entity_id: UUID) -> ModelType | None:
        """Return one active record by UUID, or None."""
        result = await self.session.execute(
            self._base_query().where(self.model.id == entity_id)
        )
        return result.scalar_one_or_none()

    async def get_all(
        self,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> Sequence[ModelType]:
        """Return active records with simple pagination."""
        statement = (
            self._base_query()
            .offset(offset)
            .limit(limit)
        )

        result = await self.session.execute(statement)
        return result.scalars().all()

    async def count(self) -> int:
        """Count active records."""
        statement = (
            select(func.count())
            .select_from(self.model)
            .where(self.model.is_deleted.is_(False))
        )

        result = await self.session.execute(statement)
        return result.scalar_one()

    async def create(self, *, data: dict[str, Any]) -> ModelType:
        """
        Create and persist one record.

        `flush()` sends SQL to PostgreSQL so generated fields are available,
        but does not permanently save until the service commits.
        """
        entity = self.model(**data)

        self.session.add(entity)
        await self.session.flush()
        await self.session.refresh(entity)

        return entity

    async def update(
        self,
        entity: ModelType,
        *,
        data: dict[str, Any],
    ) -> ModelType:
        """Apply supplied fields to an existing record."""
        for field, value in data.items():
            setattr(entity, field, value)

        await self.session.flush()
        await self.session.refresh(entity)

        return entity

    async def soft_delete(self, entity: ModelType) -> None:
        """Mark a record as deleted without removing it from PostgreSQL."""
        entity.is_deleted = True
        entity.deleted_at = datetime.now(timezone.utc)

        await self.session.flush()

    async def restore(self, entity: ModelType) -> ModelType:
        """Restore a soft-deleted record."""
        entity.is_deleted = False
        entity.deleted_at = None

        await self.session.flush()
        await self.session.refresh(entity)

        return entity