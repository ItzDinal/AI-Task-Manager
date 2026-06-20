"""upgrade task model

Revision ID: 0c058c4fbedb
Revises: 22f81405c95c
Create Date: 2026-06-20 05:05:30.458914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0c058c4fbedb'
down_revision: Union[str, Sequence[str], None] = '22f81405c95c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Create PostgreSQL enum types first
    task_priority = sa.Enum(
        "low",
        "medium",
        "high",
        "urgent",
        name="task_priority"
    )

    task_priority.create(
        op.get_bind(),
        checkfirst=True
    )

    # Add new columns
    op.add_column(
        'tasks',
        sa.Column('actual_time_spent', sa.Integer(), nullable=False, server_default='0')
    )

    op.add_column(
        'tasks',
        sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True)
    )

    op.add_column(
        'tasks',
        sa.Column('position', sa.Integer(), nullable=False, server_default='0')
    )

    op.add_column(
        'tasks',
        sa.Column('is_recurring', sa.Boolean(), nullable=False, server_default='false')
    )

    op.add_column(
        'tasks',
        sa.Column('recurrence_rule', sa.String(length=255), nullable=True)
    )

    op.add_column(
        'tasks',
        sa.Column('project_id', sa.UUID(), nullable=True)
    )

    op.add_column(
        'tasks',
        sa.Column('category_id', sa.UUID(), nullable=True)
    )

    op.add_column(
        'tasks',
        sa.Column('parent_task_id', sa.UUID(), nullable=True)
    )

    # Convert existing priority values
    # op.execute("""
    #     UPDATE tasks
    #     SET priority = UPPER(priority)
    # """)

    # Alter column to enum
    op.alter_column(
        'tasks',
        'priority',
        existing_type=sa.VARCHAR(length=50),
        type_=task_priority,
        postgresql_using='priority::task_priority',
        existing_nullable=False
    )

    op.alter_column(
        'tasks',
        'due_date',
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=True
    )

    op.alter_column(
        'tasks',
        'estimated_time',
        existing_type=sa.INTEGER(),
        nullable=False
    )

    op.create_index(
        'idx_task_due_date',
        'tasks',
        ['due_date'],
        unique=False
    )

    op.create_index(
        'idx_task_priority',
        'tasks',
        ['priority'],
        unique=False
    )

    op.create_index(
        'idx_task_user_status',
        'tasks',
        ['user_id', 'status'],
        unique=False
    )

    op.create_foreign_key(
        'fk_tasks_project_id_projects',
        'tasks',
        'projects',
        ['project_id'],
        ['id'],
        ondelete='SET NULL'
    )

    op.create_foreign_key(
        'fk_tasks_parent_task_id_tasks',
        'tasks',
        'tasks',
        ['parent_task_id'],
        ['id'],
        ondelete='CASCADE'
    )

    op.create_foreign_key(
        'fk_tasks_category_id_categories',
        'tasks',
        'categories',
        ['category_id'],
        ['id'],
        ondelete='SET NULL'
    )

    op.drop_column('tasks', 'scheduled_at')
    op.drop_column('tasks', 'priority_score')


def downgrade() -> None:
    """Downgrade schema."""

    # Restore old columns
    op.add_column(
        'tasks',
        sa.Column(
            'priority_score',
            sa.INTEGER(),
            nullable=False,
            server_default='0'
        )
    )

    op.add_column(
        'tasks',
        sa.Column(
            'scheduled_at',
            postgresql.TIMESTAMP(),
            nullable=True
        )
    )

    # Drop FKs
    op.drop_constraint(
        'fk_tasks_category_id_categories',
        'tasks',
        type_='foreignkey'
    )

    op.drop_constraint(
        'fk_tasks_parent_task_id_tasks',
        'tasks',
        type_='foreignkey'
    )

    op.drop_constraint(
        'fk_tasks_project_id_projects',
        'tasks',
        type_='foreignkey'
    )

    # Drop indexes
    op.drop_index('idx_task_user_status', table_name='tasks')
    op.drop_index('idx_task_priority', table_name='tasks')
    op.drop_index('idx_task_due_date', table_name='tasks')

    # Convert enum back to varchar
    op.alter_column(
        'tasks',
        'priority',
        existing_type=sa.Enum(
            "low",
            "medium",
            "high",
            "urgent",
            name="task_priority"
        ),
        type_=sa.VARCHAR(length=50),
        postgresql_using='priority::text',
        existing_nullable=False
    )

    op.alter_column(
        'tasks',
        'estimated_time',
        existing_type=sa.INTEGER(),
        nullable=True
    )

    op.alter_column(
        'tasks',
        'due_date',
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=True
    )

    # Drop new columns
    op.drop_column('tasks', 'parent_task_id')
    op.drop_column('tasks', 'category_id')
    op.drop_column('tasks', 'project_id')
    op.drop_column('tasks', 'recurrence_rule')
    op.drop_column('tasks', 'is_recurring')
    op.drop_column('tasks', 'position')
    op.drop_column('tasks', 'completed_at')
    op.drop_column('tasks', 'actual_time_spent')

    # Drop PostgreSQL enum type
    task_priority = sa.Enum(
        "low",
        "medium",
        "high",
        "urgent",
        name="task_priority"
    )

    task_priority.drop(
        op.get_bind(),
        checkfirst=True
    )