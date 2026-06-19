"""Compatibility re-exports for legacy imports.

The authoritative declarative base lives in ``app.db.base``. This module stays
as a thin alias so older imports can be migrated incrementally without creating
a second metadata registry.
"""

from app.db.base import Base, convention

__all__ = ["Base", "convention"]
