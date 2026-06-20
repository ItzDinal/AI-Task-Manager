# app/models/task.py

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    String,
    Text,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    Enum,
    Index,
    CheckConstraint
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import (
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin
)

from app.models.task_enums import (
    TaskStatus,
    TaskPriority
)


class Task(
    Base,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin
):
    __tablename__ = "tasks"

    # -------------------------
    # Basic Information
    # -------------------------

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    # -------------------------
    # Status & Priority
    # -------------------------

    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, name="task_status"),
        default=TaskStatus.PENDING,
        nullable=False,
        index=True
    )

    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority, name="task_priority"),
        default=TaskPriority.MEDIUM,
        nullable=False,
        index=True
    )

    # -------------------------
    # Time Tracking
    # -------------------------

    due_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        index=True
    )

    estimated_time: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    actual_time_spent: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    # -------------------------
    # Ordering
    # -------------------------

    position: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    # -------------------------
    # Recurring Tasks
    # -------------------------

    is_recurring: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    recurrence_rule: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )

    # -------------------------
    # User Relationship
    # -------------------------

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    owner = relationship(
        "User",
        back_populates="tasks"
    )

    # -------------------------
    # Project Relationship
    # -------------------------

    project_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="SET NULL"),
        nullable=True
    )

    project = relationship(
        "Project",
        back_populates="tasks"
    )

    # -------------------------
    # Category Relationship
    # -------------------------

    category_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True
    )

    category = relationship(
        "Category",
        back_populates="tasks"
    )

    # -------------------------
    # Subtasks
    # -------------------------

    parent_task_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=True
    )

    parent_task = relationship(
        "Task",
        remote_side="Task.id",
        back_populates="subtasks"
    )

    subtasks = relationship(
        "Task",
        back_populates="parent_task"
    )

    # -------------------------
    # Constraints
    # -------------------------

    __table_args__ = (
        CheckConstraint(
            "estimated_time >= 0",
            name="check_estimated_time_positive"
        ),
        CheckConstraint(
            "actual_time_spent >= 0",
            name="check_actual_time_positive"
        ),
        Index(
            "idx_task_user_status",
            "user_id",
            "status"
        ),
        Index(
            "idx_task_due_date",
            "due_date"
        ),
        Index(
            "idx_task_priority",
            "priority"
        ),
    )