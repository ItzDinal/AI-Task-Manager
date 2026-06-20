from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import UUIDMixin, TimestampMixin, SoftDeleteMixin
from app.models.task_tag import task_tags

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.task import Task


class Tag(
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin
):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    color: Mapped[str] = mapped_column(
        String(7),
        default="#8B5CF6"
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    owner: Mapped["User"] = relationship(
        "User",
        back_populates="tags"
    )
    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        secondary=task_tags,
        back_populates="tags"
    )