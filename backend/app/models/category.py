from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import UUIDMixin, TimestampMixin, SoftDeleteMixin


class Category(
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin
):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    color: Mapped[str] = mapped_column(
        String(7),
        default="#10B981"
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    owner: Mapped["User"] = relationship(
        "User",
        back_populates="categories"
    )

    # tasks: Mapped[List["Task"]] = relationship(
    #     "Task",
    #     back_populates="category"
    # )
