from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, asc, select
from typing import List, Optional
from datetime import datetime, timedelta

from app.models.task import Task
from app.models.user import User
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.core.exceptions import NotFoundError, ForbiddenError, ValidationError


# ---------------------------
# CREATE TASK
# ---------------------------
async def create_task(db: AsyncSession, task_data: TaskCreate, user_id) -> Task:
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
        await db.commit()
        await db.refresh(new_task)
    except Exception:
        await db.rollback()
        raise

    return new_task


# ---------------------------
# GET ALL TASKS (WITH FILTERS)
# ---------------------------
async def get_tasks(
    db: AsyncSession,
    user_id,
    status:Optional[str] = None,
    priority: Optional[str] = None,
    due_before: Optional[datetime] = None,
    due_after: Optional[datetime] = None,
    sort_by: str = "priority_score",
    order: str = "desc",
    limit: int = 10,
    offset: int = 0
) -> List[Task]:

    query = select(Task).where(Task.user_id == user_id)

    if status:
        query = query.where(Task.status == status)

    if priority:
        query = query.where(Task.priority == priority)

    if due_before:
        query = query.where(Task.due_date <= due_before)

    if due_after:
        query = query.where(Task.due_date >= due_after)

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

    result = await db.execute(query.offset(offset).limit(limit))
    return result.scalars().all()

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
async def get_task(db: AsyncSession, task_id: int, user_id) -> Task:
    result = await db.execute(
        select(Task).where(
            (Task.id == task_id) & (Task.user_id == user_id)
        )
    )
    task = result.scalar_one_or_none()

    if not task:
        raise NotFoundError("Task not found")

    return task


# ---------------------------
# UPDATE TASK
# ---------------------------
async def update_task(
    db: AsyncSession,
    task_id: int,
    task_data: TaskUpdate,
    user_id
) -> Task:

    task = await get_task(db, task_id, user_id)

    update_data = task_data.dict(exclude_unset=True)

    if not update_data:
        raise ValidationError("No fields provided for update")

    for key, value in update_data.items():
        setattr(task, key, value)

    try:
        await db.commit()
        await db.refresh(task)
    except Exception:
        await db.rollback()
        raise

    return task


# ---------------------------
# DELETE TASK
# ---------------------------
async def delete_task(db: AsyncSession, task_id: int, user_id) -> None:
    task = await get_task(db, task_id, user_id)

    await db.delete(task)

    try:
        await db.commit()
    except Exception:
        await db.rollback()
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
async def get_daily_plan(
        db: AsyncSession,
        user_id,
        limit: int=5
) -> List[dict]:

    # 1. Get active task (not completed)
    result = await db.execute(
        select(Task).where(
            (Task.user_id == user_id) & (Task.status != "completed")
        )
    )
    tasks = result.scalars().all()

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
                overdue_days = (task.due_date - now).days

                if overdue_days == 1:
                    urgency_bonus = 70
                    urgency_label = "overdue"

                elif overdue_days <=3:
                    urgency_bonus = 90
                    urgency_label = "overdue_high"

                else: 
                    urgency_bonus = 120
                    urgency_label = "overdue_critical"
            

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
    results.sort(key=lambda x: x["final_score"], reverse=True)

    # 6. Return top N tasks
    top_tasks = [item["task"] for item in results[:limit]]

    return top_tasks

DAILY_CAPACITY_MINUTES = 6 * 60


async def generate_schedule(
    db: AsyncSession,
    user_id,
    limit: int = 10
):
    # ---------------------------
    # 1. Get AI tasks
    # ---------------------------
    daily_tasks = await get_daily_plan(db, user_id, limit)

    candidates = []

    for task in daily_tasks:
        duration = task.estimated_time or 30

        # Calculate a simple score based on priority
        score = getattr(task, 'priority_score', 50)

        ratio = score / duration if duration > 0 else 0

        candidates.append({
            "task": task,
            "duration": duration,
            "score": score,
            "ratio": ratio,
            "urgency": "normal"
        })

    # ---------------------------
    # 🧠 Split overdue vs normal
    # ---------------------------
    overdue_tasks = []
    normal_tasks = []

    for item in candidates:
        if "overdue" in item["urgency"]:
            overdue_tasks.append(item)
        else:
            normal_tasks.append(item)

    # Sort normal tasks by greedy ratio
    normal_tasks.sort(key=lambda x: x["ratio"], reverse=True)

    selected = []
    skipped = []

    total_time = 0

    # ---------------------------
    # 🔥 STEP 1 — FORCE INCLUDE OVERDUE
    # ---------------------------
    for item in overdue_tasks:
        if total_time + item["duration"] <= DAILY_CAPACITY_MINUTES:
            selected.append(item)
            total_time += item["duration"]
        else:
            skipped.append(item)

    # ---------------------------
    # 🔥 STEP 2 — GREEDY NORMAL TASKS
    # ---------------------------
    for item in normal_tasks:
        if total_time + item["duration"] <= DAILY_CAPACITY_MINUTES:
            selected.append(item)
            total_time += item["duration"]
        else:
            skipped.append(item)

    # ---------------------------
    # ⏱️ STEP 3 — TIME SCHEDULING
    # ---------------------------
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    now = datetime.utcnow()

    start_hour = user.preferred_start_time.hour if user and user.preferred_start_time else 9
    start_min = user.preferred_start_time.minute if user and user.preferred_start_time else 0

    end_hour = user.preferred_end_time.hour if user and user.preferred_end_time else 21
    end_min = user.preferred_end_time.minute if user and user.preferred_end_time else 0

    start_time = now.replace(
        hour=start_hour,
        minute=start_min,
        second=0,
        microsecond=0
    )

    end_time_limit = now.replace(
        hour=end_hour,
        minute=end_min,
        second=0,
        microsecond=0
    )

    current_time = start_time
    schedule = []

    for item in selected:
        task = item["task"]

        task_end_time = current_time + timedelta(minutes=item["duration"])

        if task_end_time > end_time_limit:
            break

        schedule.append({
            "task": task,
            "start_time": current_time,
            "end_time": task_end_time,
            "final_score": item["score"],
            "urgency": item["urgency"]
        })

        current_time = task_end_time

    # ---------------------------
    # 📢 STEP 4 — SKIPPED TASKS
    # ---------------------------
    skipped_tasks = []

    for item in skipped:
        reason = (
            "Overdue but exceeds capacity"
            if "overdue" in item["urgency"]
            else "Not enough capacity (lower priority)"
        )

        skipped_tasks.append({
            "task": item["task"],
            "reason": reason
        })

    # ---------------------------
    # 📊 FINAL RESPONSE
    # ---------------------------
    return {
        "scheduled": schedule,
        "skipped": skipped_tasks
    }

def get_focus_task(
    db: Session,
    user_id: int
):
    schedule_data = generate_schedule(db, user_id)

    scheduled = schedule_data["scheduled"]

    if not scheduled:
        return None

    now = datetime.utcnow()

    current_task = None
    next_task = None

    for item in scheduled:
        start = item["start_time"]
        end = item["end_time"]

        # 🧠 Case 1 — current task
        if start <= now <= end:
            current_task = item
            break

        # 🧠 Case 2 — next task
        if start > now and next_task is None:
            next_task = item

    chosen = current_task or next_task

    if not chosen:
        return None

    task = chosen["task"]

    # ---------------------------
    # 🧠 Generate reason
    # ---------------------------
    reason_parts = []

    if "overdue" in chosen["urgency"]:
        reason_parts.append("Overdue task")

    elif chosen["urgency"] == "due_today":
        reason_parts.append("Due today")

    if chosen["final_score"] > 80:
        reason_parts.append("High priority")

    reason = " + ".join(reason_parts) or "Next best task"

    return {
        "task": task,
        "start_time": chosen["start_time"],
        "end_time": chosen["end_time"],
        "reason": reason
    }

def get_missed_tasks(
    db: Session,
    user_id: int
):
    now = datetime.utcnow()

    tasks = db.query(Task).filter(
        Task.user_id == user_id,
        Task.status != "completed"
    ).all()

    missed = []

    for task in tasks:
        if task.due_date and task.due_date < now:
            missed.append(task)

    return missed

def replan_day(
    db: Session,
    user_id: int
):
    # 1. Get missed tasks
    missed_tasks = get_missed_tasks(db, user_id)

    # 2. Boost missed tasks priority
    for task in missed_tasks:
        task.priority_score += 50  # 🔥 boost

    # 3. Rebuild schedule
    new_schedule = generate_schedule(db, user_id)

    return {
        "message": "Schedule updated based on missed tasks",
        "schedule": new_schedule
    }