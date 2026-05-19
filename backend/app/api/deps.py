from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User

# OAuth2 Bearer token extraction
# FastAPI will automatically read:
# Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Validate JWT token and return the authenticated user.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Decode and validate JWT token
    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    # Extract user identity from JWT payload
    email: str | None = payload.get("sub")

    if email is None:
        raise credentials_exception

    # Fetch user from database
    result = await db.execute(
        select(User).where(User.email == email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(
    current_user: Annotated[
        User,
        Depends(get_current_user)
    ]
) -> User:
    """
    Ensure authenticated user is active.
    """

    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return current_user