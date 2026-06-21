from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.api.error_handlers import raise_http_error
from app.db.session import get_db
from app.models.task_enums import TaskPriority, TaskStatus
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.exceptions import ServiceError
from app.services.task_service import TaskService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    data: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TaskResponse:
    """Create a task for the authenticated user."""
    service = TaskService(db)

    try:
        return await service.create_task(current_user.id, data)
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "",
    response_model=list[TaskResponse],
)
async def list_tasks(
    status_filter: TaskStatus | None = Query(default=None, alias="status"),
    priority: TaskPriority | None = Query(default=None),
    project_id: UUID | None = Query(default=None),
    category_id: UUID | None = Query(default=None),
    due_before: datetime | None = Query(default=None),
    due_after: datetime | None = Query(default=None),
    include_completed: bool = Query(default=True),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[TaskResponse]:
    """List filtered tasks owned by the authenticated user."""
    service = TaskService(db)

    try:
        return await service.get_tasks(
            current_user.id,
            status=status_filter,
            priority=priority,
            project_id=project_id,
            category_id=category_id,
            due_before=due_before,
            due_after=due_after,
            include_completed=include_completed,
            offset=offset,
            limit=limit,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
async def get_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TaskResponse:
    """Get one task owned by the authenticated user."""
    service = TaskService(db)

    try:
        return await service.get_task(task_id, current_user.id)
    except ServiceError as error:
        raise_http_error(error)


@router.patch(
    "/{task_id}",
    response_model=TaskResponse,
)
async def update_task(
    task_id: UUID,
    data: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TaskResponse:
    """Partially update a task owned by the authenticated user."""
    service = TaskService(db)

    try:
        return await service.update_task(
            task_id,
            current_user.id,
            data,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    """Soft-delete one task owned by the authenticated user."""
    service = TaskService(db)

    try:
        await service.delete_task(task_id, current_user.id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "/{task_id}/subtasks",
    response_model=list[TaskResponse],
)
async def get_subtasks(
    task_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[TaskResponse]:
    """Get subtasks for a task owned by the authenticated user."""
    service = TaskService(db)

    try:
        return await service.get_subtasks(task_id, current_user.id)
    except ServiceError as error:
        raise_http_error(error)