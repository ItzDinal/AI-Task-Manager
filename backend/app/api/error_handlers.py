from fastapi import HTTPException, status

from app.services.exceptions import (
    ConflictError,
    ForbiddenError,
    NotFoundError,
    ServiceError,
    ValidationError,
)


def raise_http_error(error: ServiceError) -> None:
    """
    Convert service-layer errors into consistent FastAPI HTTP errors.

    Services stay independent from FastAPI; routes call this helper when
    a business-rule exception occurs.
    """

    if isinstance(error, NotFoundError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error.message,
        )

    if isinstance(error, ConflictError):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        )

    if isinstance(error, ForbiddenError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=error.message,
        )

    if isinstance(error, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=error.message,
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=error.message,
    )