from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import RequestValidationError
from fastapi import status
from profiles.exceptions import UserProfileNotFound, DuplicateUsernameException

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation failed",
            "details": exc.errors()
        }
    )

def add_custom_exception_handlers(app):
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(UserProfileNotFound, lambda request, exc: JSONResponse(status_code=exc.status_code, content=exc.detail))
    app.add_exception_handler(DuplicateUsernameException, lambda request, exc: JSONResponse(status_code=exc.status_code, content=exc.detail))