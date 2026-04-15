class DatabaseError(Exception):
    """Base database exception."""
    pass


class DuplicateEntryError(DatabaseError):
    """Raised when duplicate entry occurs."""
    pass


class DatabaseConnectionError(DatabaseError):
    """Raised when DB connection fails."""
    pass


class NotFoundError(Exception):
    pass

class ForbiddenError(Exception):
    pass

class ValidationError(Exception):
    pass