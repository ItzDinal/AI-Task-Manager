# app/api/schedule_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.services.schedule_service import run_scheduler
from app.schemas.task import TaskResponse
from app.api.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/schedule", tags=["Scheduling"])


@router.post("/", response_model=list[TaskResponse])
async def generate_schedule(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    scheduled_tasks = await run_scheduler(db, current_user.id)

    return scheduled_tasks