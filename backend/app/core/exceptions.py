class DatabaseError(Exception):
    """Base database exception."""
    pass


class DuplicateEntryError(DatabaseError):
    """Raised when duplicate entry occurs."""
    pass


class DatabaseConnectionError(DatabaseError):
    """Raised when DB connection fails."""
    pass