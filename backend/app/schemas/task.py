from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, field_validator

from app.models.task_enums import TaskPriority, TaskStatus
from app.schemas.common import SchemaBase, TimestampResponse
from app.schemas.tag import TagResponse


class TaskCreate(SchemaBase):
    """Schema used when creating a task."""

    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        examples=["Finish Phase 2 schemas"],
    )
    description: Optional[str] = Field(default=None, max_length=5000)

    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM

    due_date: Optional[datetime] = None
    estimated_time: int = Field(default=0, ge=0)

    project_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    parent_task_id: Optional[UUID] = None

    position: int = Field(default=0, ge=0)
    is_recurring: bool = False
    recurrence_rule: Optional[str] = Field(default=None, max_length=255)

    tag_ids: list[UUID] = Field(default_factory=list)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Task title cannot be empty")
        return value.strip()

    @field_validator("recurrence_rule")
    @classmethod
    def validate_recurrence_rule(
        cls,
        value: Optional[str],
    ) -> Optional[str]:
        return value.strip() if value and value.strip() else None


class TaskUpdate(SchemaBase):
    """Schema used when partially updating a task."""

    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=5000)

    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None

    due_date: Optional[datetime] = None
    estimated_time: Optional[int] = Field(default=None, ge=0)
    actual_time_spent: Optional[int] = Field(default=None, ge=0)

    project_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    parent_task_id: Optional[UUID] = None

    position: Optional[int] = Field(default=None, ge=0)
    is_recurring: Optional[bool] = None
    recurrence_rule: Optional[str] = Field(default=None, max_length=255)

    tag_ids: Optional[list[UUID]] = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Task title cannot be empty")
        return value.strip() if value is not None else value

    @field_validator("recurrence_rule")
    @classmethod
    def validate_recurrence_rule(
        cls,
        value: Optional[str],
    ) -> Optional[str]:
        return value.strip() if value and value.strip() else None


class TaskResponse(TimestampResponse):
    """Schema returned from task API endpoints."""

    title: str
    description: Optional[str] = None

    status: TaskStatus
    priority: TaskPriority

    due_date: Optional[datetime] = None
    estimated_time: int
    actual_time_spent: int

    completed_at: Optional[datetime] = None

    position: int
    is_recurring: bool
    recurrence_rule: Optional[str] = None

    user_id: UUID
    project_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    parent_task_id: Optional[UUID] = None

    tags: list[TagResponse] = Field(default_factory=list)


class TaskListResponse(SchemaBase):
    """Paginated task-list response."""

    items: list[TaskResponse]
    total: int
    page: int
    page_size: int