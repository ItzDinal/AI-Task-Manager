# app/schemas/task.py

from datetime import datetime
from typing import Optional, Literal
from uuid import UUID

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"
    due_date: Optional[datetime] = None
    estimated_time: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["pending", "in_progress", "completed"]] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    estimated_time: Optional[int] = None


class TaskResponse(TaskBase):
    id: UUID
    status: str
    user_id: UUID
    priority_score: int
    scheduled_at: Optional[datetime] = None
    completed: bool

    class Config:
        from_attributes = True