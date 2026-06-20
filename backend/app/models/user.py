import uuid
from typing import Optional, List

from sqlalchemy import String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import UserRole
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.project import Project
    from app.models.task import Task
    from app.models.tag import Tag
from app.models.mixins import (
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin
)
from typing import List



class User(
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin):
    """User model for authentication system."""

    __tablename__ = "users"

    # id: Mapped[uuid.UUID] = mapped_column(
    #     UUID(as_uuid=True),
    #     primary_key=True,
    #     default=uuid.uuid4
    # )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    full_name: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        default=UserRole.USER,
        nullable=False
    )

    projects: Mapped[List["Project"]] = relationship(
        "Project",
        back_populates="owner",
        cascade="all, delete-orphan"
    )
    categories: Mapped[List["Category"]] = relationship(
        "Category",
        back_populates="owner",
        cascade="all, delete-orphan"
    )
    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    tags: Mapped[List["Tag"]] = relationship(
        "Tag",
        back_populates="owner",
        cascade="all, delete-orphan"
    )