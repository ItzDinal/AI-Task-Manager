# app/schemas/task_schema.py

import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from typing import Literal


# ---------------------------
# BASE SCHEMA (SHARED FIELDS)
# ---------------------------
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)

    priority: Literal["low", "medium", "high"] = "medium"

    due_date: Optional[datetime] = None
    estimated_time: Optional[int] = Field(None, ge=0)



# ---------------------------
# CREATE SCHEMA
# ---------------------------
class TaskCreate(TaskBase):
    pass


# ---------------------------
# UPDATE SCHEMA (ALL OPTIONAL)
# ---------------------------
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)

    priority: Optional[Literal["low", "medium", "high"]] = None

    due_date: Optional[datetime] = None
    estimated_time: Optional[int] = Field(None, ge=0)

    status: Optional[Literal["pending", "in_progress", "completed"]] = None

# ---------------------------
# RESPONSE SCHEMA
# ---------------------------
class TaskResponse(BaseModel):
    id: uuid.UUID

    title: str
    description: Optional[str]

    priority: str
    status: str

    due_date: Optional[datetime]
    estimated_time: Optional[int]

    priority_score: int
    scheduled_at: Optional[datetime] = None

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

# ---------------------------
# 📅 DAILY PLANNER RESPONSE
# ---------------------------
class DailyTaskResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str]

    priority: str
    status: str

    due_date: Optional[datetime]
    estimated_time: Optional[int]

    priority_score: int

    final_score: int
    urgency: str

    model_config = {
        "from_attributes": True
    }