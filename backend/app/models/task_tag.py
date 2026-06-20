from sqlalchemy import Table, Column, ForeignKey

from app.db.base import Base

task_tags = Table(
    "task_tags",
    Base.metadata,

    Column(
        "task_id",
        ForeignKey("tasks.id", ondelete="CASCADE"),
        primary_key=True
    ),

    Column(
        "tag_id",
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True
    )
)