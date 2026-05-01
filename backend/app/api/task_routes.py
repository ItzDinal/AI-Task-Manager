# app/api/task_routes.py

from fastapi import APIRouter, Depends
from fastapi import Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Literal
from uuid import UUID
from datetime import datetime

from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services import task_service
from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.task_schema import DailyTaskResponse, ScheduleItem, SkippedItem, ScheduleResponse, FocusTaskResponse


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("", response_model=TaskResponse, status_code=201)
async def create_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.create_task(db, task, current_user.id)


@router.get("", response_model=list[TaskResponse])
async def get_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    due_before: datetime | None = None,
    due_after: datetime | None = None,
    sort_by: Optional[str] = "priority_score",
    order: Literal["asc", "desc"] = "desc",
    limit: int = Query(10, ge=1 ,le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.get_tasks(
        db=db,
        user_id=current_user.id,
        status=status,
        priority=priority,
        due_before=due_before,
        due_after=due_after,
        sort_by=sort_by,
        order=order,
        limit=limit,
        offset=offset
    )


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.get_task(db, task_id, current_user.id)


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: UUID,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.update_task(
        db,
        task_id,
        task,
        current_user.id
    )


@router.delete("/{task_id}", status_code=204)
async def delete_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await task_service.delete_task(
        db,
        task_id,
        current_user.id
    )

@router.get("/daily-plan", response_model=list[DailyTaskResponse])
async def get_daily_plan(
    limit: int = Query(5, ge=1,  le=10),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await task_service.get_daily_plan(
        db=db,
        user_id=current_user.id,
        limit=limit
    )

    response = []

    for item in result:
        task = item

        response.append(DailyTaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            priority=task.priority,
            due_date=task.due_date,
            estimated_time=task.estimated_time,
            priority_score=task.priority_score,
            final_score=50,
            urgency="normal"
        ))

    return response

from app.schemas.task_schema import ScheduleTaskResponse


@router.get("/schedule", response_model=ScheduleResponse)
async def get_schedule(
    limit: int = Query(10, ge=1, le=20),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await task_service.generate_schedule(
        db=db,
        user_id=current_user.id,
        limit=limit
    )

    scheduled_response = []
    skipped_response = []

    # Schedule tasks
    for item in result["scheduled"]:
        task = item["task"]

        scheduled_response.append(ScheduleTaskResponse(
            id=task.id,
            title=task.title,
            start_time=item["start_time"],
            end_time=item["end_time"],
            priority_score=task.priority_score,
            final_score=item["final_score"],
            urgency=item["urgency"]
        ))
    
    for item in result["skipped"]:
        task = item["task"]

        skipped_response.append(SkippedItem(
            id=task.id,
            title=task.title,
            reason=item["reason"]
        ))

    return ScheduleResponse(
        scheduled=scheduled_response,
        skipped=skipped_response
    )

@router.get("/focus", response_model=FocusTaskResponse | None)
async def get_focus_task(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = task_service.get_focus_task(
        db=db,
        user_id=current_user.id
    )

    if not result:
        return None

    task = result["task"]

    return FocusTaskResponse(
        id=task.id,
        title=task.title,
        start_time=result["start_time"],
        end_time=result["end_time"],
        reason=result["reason"]
    )

@router.post("/replan")
async def replan_tasks(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = task_service.replan_day(
        db=db,
        user_id=current_user.id
    )

    return result