class ServiceError(Exception):
    """Base exception for all application service errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class NotFoundError(ServiceError):
    """Raised when a requested resource does not exist."""


class ConflictError(ServiceError):
    """Raised when an operation would create duplicate/conflicting data."""


class ForbiddenError(ServiceError):
    """Raised when a user tries to access a resource they do not own."""


class ValidationError(ServiceError):
    """Raised when related data or business rules are invalid."""