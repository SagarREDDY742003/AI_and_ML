class APIError(Exception):
    """Base class for API errors."""
    pass

class AuthenticationError(APIError):
    """Raised when authentication fails."""
    pass

class NotFoundError(APIError):
    """Raised when resource is not found."""
    pass