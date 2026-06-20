from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, field_validator

from app.schemas.common import SchemaBase, TimestampResponse


class ProjectCreate(SchemaBase):
    """Schema used when creating a project."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=255,
        examples=["AI Task Manager"]
    )

    description: Optional[str] = Field(
        default=None,
        max_length=5000,
        examples=["Backend development tasks and milestones."]
    )

    color: str = Field(
        default="#3B82F6",
        pattern=r"^#[0-9A-Fa-f]{6}$",
        examples=["#3B82F6"]
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Project name cannot be empty")
        return value.strip()


class ProjectUpdate(SchemaBase):
    """Schema used when partially updating a project."""

    name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    description: Optional[str] = Field(
        default=None,
        max_length=5000
    )

    color: Optional[str] = Field(
        default=None,
        pattern=r"^#[0-9A-Fa-f]{6}$"
    )

    is_archived: Optional[bool] = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Project name cannot be empty")
        return value.strip() if value is not None else value


class ProjectResponse(TimestampResponse):
    """Schema returned from project API endpoints."""

    name: str
    description: Optional[str] = None
    color: str
    is_archived: bool
    user_id: UUID