from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from typing import Any

from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError
from passlib.context import CryptContext

from app.core.config import settings

# Compatibility shim for passlib with newer bcrypt releases.
# passlib's backend checks rely on legacy bcrypt behavior for >72-byte inputs.
try:
    import bcrypt as _bcrypt

    if not hasattr(_bcrypt, "__about__"):
        _bcrypt.__about__ = SimpleNamespace(__version__=getattr(_bcrypt, "__version__", "unknown"))

    _original_hashpw = _bcrypt.hashpw

    def _passlib_compatible_hashpw(password: bytes, salt: bytes) -> bytes:
        try:
            return _original_hashpw(password, salt)
        except ValueError as exc:
            if "longer than 72 bytes" in str(exc):
                return _original_hashpw(password[:72], salt)
            raise

    _bcrypt.hashpw = _passlib_compatible_hashpw
except Exception:
    # If bcrypt is unavailable or immutable, passlib will raise explicit errors on use.
    pass

# Central password hashing context (bcrypt with safe defaults from passlib)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a plain-text password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against a stored bcrypt hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict[str, Any]) -> str:
    """Create a signed JWT access token with an expiration claim."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode["exp"] = expire

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Decode and validate a JWT access token."""
    try:
        payload: dict[str, Any] = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        return payload
    except ExpiredSignatureError:
        return None
    except JWTError:
        return None
