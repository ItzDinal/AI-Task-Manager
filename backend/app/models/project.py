from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import UUIDMixin, TimestampMixin, SoftDeleteMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User

class Project(
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin
):
    __tablename__ = "projects"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    color: Mapped[str] = mapped_column(
        String(7),
        default="#3B82F6"
    )

    is_archived: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    owner = relationship(
        "User",
        back_populates="projects"
    )

    tasks = relationship(
        "Task",
        back_populates="project"
    )