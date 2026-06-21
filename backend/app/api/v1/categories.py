from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.api.error_handlers import raise_http_error
from app.db.session import get_db
from app.models.user import User
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from app.services.category_service import CategoryService
from app.services.exceptions import ServiceError


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    data: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CategoryResponse:
    """Create a category for the authenticated user."""
    service = CategoryService(db)

    try:
        return await service.create_category(current_user.id, data)
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "",
    response_model=list[CategoryResponse],
)
async def list_categories(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[CategoryResponse]:
    """List categories owned by the authenticated user."""
    service = CategoryService(db)

    try:
        return await service.get_categories(
            current_user.id,
            offset=offset,
            limit=limit,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
async def get_category(
    category_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CategoryResponse:
    """Get one category owned by the authenticated user."""
    service = CategoryService(db)

    try:
        return await service.get_category(category_id, current_user.id)
    except ServiceError as error:
        raise_http_error(error)


@router.patch(
    "/{category_id}",
    response_model=CategoryResponse,
)
async def update_category(
    category_id: UUID,
    data: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CategoryResponse:
    """Partially update one category owned by the authenticated user."""
    service = CategoryService(db)

    try:
        return await service.update_category(
            category_id,
            current_user.id,
            data,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_category(
    category_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    """Soft-delete one category owned by the authenticated user."""
    service = CategoryService(db)

    try:
        await service.delete_category(category_id, current_user.id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ServiceError as error:
        raise_http_error(error)
        