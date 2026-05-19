from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_active_user
from app.core.security import create_access_token, hash_password, verify_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import Token, UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])



@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
) -> UserResponse:
    """
    Register a new user account.
    """
    existing_user = await db.scalar(
        select(User).where(User.email == user_in.email)
    )
    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Temporary username strategy: derive from email local-part.
    # This keeps auth flow functional until username is explicitly captured.
    derived_username = user_in.email.split("@", 1)[0]

    user = User(
        email=user_in.email,
        username=derived_username,
        hashed_password=hash_password(user_in.password),
    )
    db.add(user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unable to register user with provided credentials",
        )

    await db.refresh(user)
    return user


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
) -> Token:
    """
    Authenticate user by email and issue JWT access token.
    """
    user = await db.scalar(
        select(User).where(User.email == form_data.username)
    )

    if user is None or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token({"sub": user.email})
    return Token(
        access_token=access_token,
        token_type="bearer",
    )


@router.get("/me", response_model=UserResponse)
async def read_current_user(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> UserResponse:
    """
    Return current authenticated active user.
    """
    return current_user
