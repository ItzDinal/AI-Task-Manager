from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List, Optional
from datetime import datetime, timedelta

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
# ---------------------------
# Date Time Planner (AI)
# ---------------------------
def get_daily_plan(
        db: Session,
        user_id: int,
        limit: int=5
) -> List[dict]:

    # 1. Get active task (not completed)
    tasks = db.query(Task).filter(
        Task.user_id == user_id,
        Task.status != "completed"
    ).all()

    results = []
    now = datetime.utcnow()

    for task in tasks:
        # 2. Base Score
        base_score = task.priority_score or 0

        # 3. Urgency bonus
        urgency_bonus = 0 

        urgency_label = "none"

        if task.due_date:
            days_left = (task.due_date - now).days

            if days_left < 0:
                urgency_bonus = 70 # overdue
                urgency_label = "Overdue"
            elif days_left == 0:
                urgency_bonus = 50 # today
                urgency_label = "due_today"

            elif days_left <= 2:
                urgency_bonus = 30 # soon
                urgency_label = "due_soon"


        # 4. Final Score
        final_score = base_score + urgency_bonus

        results.append({
            "task": task,
            "final_score": final_score,
            "urgency": urgency_label
        })
    # 5. Sort by AI score
    results.sort(key=lambda x: x["fina_score"], reverse=True)

    # 6. Return top N tasks
    top_tasks = [item[task]for item in results[:limit]]

    return top_tasks

# ---------------------------
# ⏱️ TIME ALLOCATION ENGINE
# ---------------------------
def generate_schedule(
    db: Session,
    user_id: int,
    limit: int = 5
):

    # 1. Get AI-selected tasks
    daily_tasks = get_daily_plan(db, user_id, limit)

    # 2. Define working hours
    start_time = datetime.utcnow().replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = datetime.utcnow().replace(hour=21, minute=0, second=0, microsecond=0)

    current_time = start_time
    schedule = []

    for item in daily_tasks:
        task = item["task"]

        # Default duration = 30 mins if not set
        duration_minutes = task.estimated_time or 30

        task_end_time = current_time + timedelta(minutes=duration_minutes)

        # Stop if exceeds day limit
        if task_end_time > end_time:
            break

        schedule.append({
            "task": task,
            "start_time": current_time,
            "end_time": task_end_time,
            "final_score": item["final_score"],
            "urgency": item["urgency"]
        })

        # Move time forward
        current_time = task_end_time

    return schedule