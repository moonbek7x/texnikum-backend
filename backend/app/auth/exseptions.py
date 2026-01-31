from fastapi import HTTPException, status


class AuthException(HTTPException):
    status_code = 500
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(AuthException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User with this login already exists"

class InvalidCredentialsException(AuthException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect login or password"

class UserNotFound(AuthException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User not found"
