from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.api.error_handlers import raise_http_error
from app.db.session import get_db
from app.models.user import User
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from app.services.exceptions import ServiceError
from app.services.project_service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_project(
    data: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ProjectResponse:
    """Create a project for the authenticated user."""
    service = ProjectService(db)

    try:
        return await service.create_project(current_user.id, data)
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "",
    response_model=list[ProjectResponse],
)
async def list_projects(
    include_archived: bool = Query(default=False),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[ProjectResponse]:
    """List projects owned by the authenticated user."""
    service = ProjectService(db)

    try:
        return await service.get_projects(
            current_user.id,
            include_archived=include_archived,
            offset=offset,
            limit=limit,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ProjectResponse:
    """Get one project owned by the authenticated user."""
    service = ProjectService(db)

    try:
        return await service.get_project(project_id, current_user.id)
    except ServiceError as error:
        raise_http_error(error)


@router.patch(
    "/{project_id}",
    response_model=ProjectResponse,
)
async def update_project(
    project_id: UUID,
    data: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ProjectResponse:
    """Partially update one project owned by the authenticated user."""
    service = ProjectService(db)

    try:
        return await service.update_project(
            project_id,
            current_user.id,
            data,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    """Soft-delete one project owned by the authenticated user."""
    service = ProjectService(db)

    try:
        await service.delete_project(project_id, current_user.id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ServiceError as error:
        raise_http_error(error)