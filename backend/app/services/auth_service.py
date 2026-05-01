from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password, create_access_token 

async def create_user(db: AsyncSession, user_data: UserCreate):
    # Check if user already exists
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise ValueError("Email already registered")

    # Hash password
    hashed_password = hash_password(user_data.password)

    # Create user object
    new_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password
    )

    # Save to DB
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

async def authenticate_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user

def create_user_token(user: User):
    token_data = {"sub": str(user.id)}
    access_token = create_access_token(token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users