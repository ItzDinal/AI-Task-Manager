# app/services/task_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from datetime import datetime

from app.models.task import Task

# Enforce workflow transitions (VERY IMPORTANT)
def validate_status_transition(current_status, new_status):
    valid_transitions = {
        "pending": ["in_progress", "completed"],
        "in_progress": ["completed"],
        "completed": []
    }

    if new_status not in valid_transitions[current_status]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status transition from {current_status} to {new_status}"
        )
    
async def create_task(db: AsyncSession, task_data, user_id):
    task = Task(**task_data.dict(), user_id=user_id)

    db.add(task)
    await db.commit()
    await db.refresh(task)

    return task


async def get_tasks(
        db: AsyncSession, 
        user_id, 
        status=None, 
        priority=None,
        due_before=None,
        due_after=None,
        sort_by="created_at",
        order="desc",
        limit=10,
        offset=0
        ):
    query = select(Task).where(Task.user_id == user_id)

    if status:
        query = query.where(Task.status == status)

    if priority:
        query = query.where(Task.priority == priority)

    if due_before:
        query = query.where(Task.due_date <= datetime.fromisoformat(due_before))

    if due_after:
        query = query.where(Task.due_date >= datetime.fromisoformat(due_after))

    # 🔄 SORTING
    sort_column = getattr(Task, sort_by, Task.created_at)

    if order == "asc":
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())
    
    # 📄 PAGINATION
    query = query.limit(limit).offset(offset)

    result = await db.execute(query)
    return result.scalars().all()


async def get_task(db: AsyncSession, task_id, user_id):
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    return task


async def update_task(db: AsyncSession, task_id, task_data, user_id):
    task = await get_task(db, task_id, user_id)

    update_data = task_data.dict(exclude_unset=True)

    if "status" in update_data:
        validate_status_transition(task.status, update_data["status"])


    for key, value in update_data.items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)

    return task


async def delete_task(db: AsyncSession, task_id, user_id):
    task = await get_task(db, task_id, user_id)

    await db.delete(task)
    await db.commit()

    return {"message": "Task deleted"}