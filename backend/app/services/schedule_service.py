# app/services/schedule_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.task import Task
from app.services.scheduler_service import generate_schedule


async def get_active_tasks_by_user(db: AsyncSession, user_id):
    result = await db.execute(
        select(Task).where(Task.user_id == user_id)
    )

    tasks = result.scalars().all()

    # Filter active tasks
    return [
        t for t in tasks
        if t.status != "completed" and not t.completed
    ]


async def run_scheduler(db: AsyncSession, user_id):
    # 🔹 1. Fetch tasks
    tasks = await get_active_tasks_by_user(db, user_id)

    if not tasks:
        return []

    # 🔹 2. Generate schedule
    scheduled_tasks = generate_schedule(tasks)

    # 🔹 3. Persist updates
    for task in scheduled_tasks:
        db.add(task)

    await db.commit()

    # 🔹 4. Refresh (optional but recommended)
    for task in scheduled_tasks:
        await db.refresh(task)

    return scheduled_tasks