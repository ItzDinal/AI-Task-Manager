from typing import Optional
from uuid import UUID

from pydantic import Field, field_validator

from app.schemas.common import TimestampResponse, SchemaBase


class CategoryCreate(SchemaBase):
    """Schema used when creating a category."""

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        examples=["Work"]
    )

    color: str = Field(
        default="#10B981",
        pattern=r"^#[0-9A-Fa-f]{6}$",
        examples=["#10B981"]
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Category name cannot be empty")
        return value.strip()


class CategoryUpdate(SchemaBase):
    """Schema used when partially updating a category."""

    name: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    color: Optional[str] = Field(
        default=None,
        pattern=r"^#[0-9A-Fa-f]{6}$"
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Category name cannot be empty")
        return value.strip() if value is not None else value


class CategoryResponse(TimestampResponse):
    """Schema returned from category API endpoints."""

    name: str
    color: str
    user_id: UUID
    