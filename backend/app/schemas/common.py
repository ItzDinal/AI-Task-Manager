from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SchemaBase(BaseModel):
    """Base configuration shared by all API schemas."""

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        str_strip_whitespace=True
    )


class TimestampResponse(SchemaBase):
    """Reusable timestamps returned by the API."""

    id: UUID
    created_at: datetime
    updated_at: datetime


class SoftDeleteResponse(SchemaBase):
    """Reusable soft-delete state returned by the API."""

    is_deleted: bool
    deleted_at: Optional[datetime] = None