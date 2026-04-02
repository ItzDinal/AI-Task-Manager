# app/models/task.py

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text, DateTime, ForeignKey, Integer, Enum, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel

STATUS_PENDING = "pending"
STATUS_IN_PROGRESS = "in_progress"
STATUS_COMPLETED = "completed"

ALLOWED_STATUSES = [
    STATUS_PENDING,
    STATUS_IN_PROGRESS,
    STATUS_COMPLETED
]

class Task(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    status: Mapped[str] = mapped_column(
        Enum(*ALLOWED_STATUSES, name="task_status"),
        default=STATUS_PENDING
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="medium"
    )

    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    estimated_time: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True
    )  # minutes

    # AI / Scheduling Fields

    # Calculated numeric score
    priority_score: Mapped[int] = mapped_column(Integer, default=0)

    # When task is scheduled
    scheduled_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    # Optional explicit completion flag (can derive from status too)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    # 🔐 CRITICAL: User ownership
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    # Relationship
    user = relationship("User", back_populates="tasks")

    