from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List, Optional
from datetime import datetime

from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.core.exceptions import NotFoundError, ForbiddenError, ValidationError


# ---------------------------
# CREATE TASK
# ---------------------------
def create_task(db: Session, task_data: TaskCreate, user_id: int) -> Task:
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        due_date=task_data.due_date,
        priority=task_data.priority,
        status="pending",
        user_id=user_id
    )

    db.add(new_task)

    try:
        db.commit()
        db.refresh(new_task)
    except Exception:
        db.rollback()
        raise

    return new_task


# ---------------------------
# GET ALL TASKS (WITH FILTERS)
# ---------------------------
def get_tasks(
    db: Session,
    user_id: int,
    status:Optional[str] = None,
    priority: Optional[str] = None,
    due_before: Optional[datetime] = None,
    due_after: Optional[datetime] = None,
    sort_by: str = "priority_score",
    order: str = "desc",
    limit: int = 10,
    offset: int = 0
) -> List[Task]:

    query = db.query(Task).filter(Task.user_id == user_id)

    if status:
        query = query.filter(Task.status == status)

    if priority:
        query = query.filter(Task.priority == priority)

    if due_before:
        query = query.filter(Task.due_date <= due_before)

    if due_after:
        query = query.filter(Task.due_date >= due_after)

    if sort_by == "priority_score":
        column = Task.priority_score

    elif sort_by == "due_date":
        column = Task.due_date

    elif sort_by == "created_at":
        column = Task.created_at
    
    else:
        raise ValidationError(f"Invalid sort field: {sort_by}")
    
     # Apply order
    if order == "desc":
        query = query.order_by(desc(column))
    else:
        query = query.order_by(asc(column))

    return query.offset(offset).limit(limit).all()

    # # Safe sorting
    # allowed_sort_fields = {"created_at", "due_date", "priority"}
    # if sort_by not in allowed_sort_fields:
    #     raise ValidationError(f"Invalid sort field: {sort_by}")

    # column = getattr(Task, sort_by)

    # if order == "desc":
    #     query = query.order_by(column.desc())
    # else:
    #     query = query.order_by(column.asc())

    # return query.offset(offset).limit(limit).all()


# ---------------------------
# GET SINGLE TASK (SECURE)
# ---------------------------
def get_task(db: Session, task_id: int, user_id: int) -> Task:
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if not task:
        raise NotFoundError("Task not found")

    return task


# ---------------------------
# UPDATE TASK
# ---------------------------
def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate,
    user_id: int
) -> Task:

    task = get_task(db, task_id, user_id)

    update_data = task_data.dict(exclude_unset=True)

    if not update_data:
        raise ValidationError("No fields provided for update")

    for key, value in update_data.items():
        setattr(task, key, value)

    try:
        db.commit()
        db.refresh(task)
    except Exception:
        db.rollback()
        raise

    return task


# ---------------------------
# DELETE TASK
# ---------------------------
def delete_task(db: Session, task_id: int, user_id: int) -> None:
    task = get_task(db, task_id, user_id)

    db.delete(task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise


# ---------------------------
# STATUS TRANSITION VALIDATION
# ---------------------------
def validate_status_transition(current_status: str, new_status: str):
    valid_transitions = {
        "pending": ["in_progress", "completed"],
        "in_progress": ["completed"],
        "completed": []
    }

    allowed = valid_transitions.get(current_status)

    if not allowed:
        raise ValidationError("Invalid current status")

    if new_status not in allowed:
        raise ValidationError(
            f"Cannot change status from {current_status} to {new_status}"
        )