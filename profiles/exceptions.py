from fastapi import HTTPException, status

class UserProfileNotFound(HTTPException):
    def __init__(self, username: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "User profile not found", "username": username}
        )

class DuplicateUsernameException(HTTPException):
    def __init__(self, username: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail={"error": "Duplicate username", "username": username}
        )