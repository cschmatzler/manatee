from __future__ import annotations  # TODO: Remove in Python 3.10

from fastapi.exceptions import HTTPException as FastAPIHTTPException
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)


class HTTPException(FastAPIHTTPException):
    def __init__(
        self, type: str, message: str, status_code: int = 500, headers: dict = {}
    ):
        super().__init__(
            status_code=status_code,
            headers=headers,
            detail=[{"msg": message, "type": type}],
        )


class UnauthorizedException(HTTPException):
    def __init__(self, type: str, message: str):
        super().__init__(type, message, status_code=HTTP_401_UNAUTHORIZED)


class ForbiddenException(HTTPException):
    def __init__(self, type: str, message: str):
        super().__init__(type, message, status_code=HTTP_403_FORBIDDEN)


class NotFoundException(HTTPException):
    def __init__(self, type: str, message: str):
        super().__init__(type, message, status_code=HTTP_404_NOT_FOUND)


class ConflictException(HTTPException):
    def __init__(self, type: str, message: str):
        super().__init__(type, message, status_code=HTTP_409_CONFLICT)
