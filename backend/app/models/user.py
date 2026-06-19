from datetime import time
from typing import Optional, List

from sqlalchemy import String, Boolean, Enum, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import UserRole
from app.models.mixins import SoftDeleteMixin, TimestampMixin, UUIDMixin


class User(UUIDMixin, TimestampMixin, SoftDeleteMixin, Base):
    """User model for authentication system."""

    __tablename__ = "users"

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

    # ---------------------------
    # 🧠 TIME PREFERENCE (NEW)
    # ---------------------------
    preferred_start_time: Mapped[Optional[time]] = mapped_column(
        Time,
        nullable=True
    )

    preferred_end_time: Mapped[Optional[time]] = mapped_column(
        Time,
        nullable=True
    )

    # ---------------------------
    # 🔗 RELATIONSHIPS
    # ---------------------------
    tasks: Mapped[List["Task"]] = relationship(
        "Task",
        back_populates="user",
        cascade="all, delete"
    )
