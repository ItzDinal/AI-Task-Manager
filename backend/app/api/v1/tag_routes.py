from uuid import UUID

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.api.error_handlers import raise_http_error
from app.db.session import get_db
from app.models.user import User
from app.schemas.tag import TagCreate, TagResponse, TagUpdate
from app.services.exceptions import ServiceError
from app.services.tag_service import TagService


router = APIRouter(
    prefix="/tags",
    tags=["Tags"],
)


@router.post(
    "",
    response_model=TagResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_tag(
    data: TagCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TagResponse:
    """Create a tag for the authenticated user."""
    service = TagService(db)

    try:
        return await service.create_tag(current_user.id, data)
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "",
    response_model=list[TagResponse],
)
async def list_tags(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[TagResponse]:
    """List tags owned by the authenticated user."""
    service = TagService(db)

    try:
        return await service.get_tags(
            current_user.id,
            offset=offset,
            limit=limit,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.get(
    "/{tag_id}",
    response_model=TagResponse,
)
async def get_tag(
    tag_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TagResponse:
    """Get one tag owned by the authenticated user."""
    service = TagService(db)

    try:
        return await service.get_tag(tag_id, current_user.id)
    except ServiceError as error:
        raise_http_error(error)


@router.patch(
    "/{tag_id}",
    response_model=TagResponse,
)
async def update_tag(
    tag_id: UUID,
    data: TagUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> TagResponse:
    """Partially update one tag owned by the authenticated user."""
    service = TagService(db)

    try:
        return await service.update_tag(
            tag_id,
            current_user.id,
            data,
        )
    except ServiceError as error:
        raise_http_error(error)


@router.delete(
    "/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_tag(
    tag_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Response:
    """Soft-delete one tag owned by the authenticated user."""
    service = TagService(db)

    try:
        await service.delete_tag(tag_id, current_user.id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ServiceError as error:
        raise_http_error(error)