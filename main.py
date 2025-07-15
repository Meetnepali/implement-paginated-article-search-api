from fastapi import FastAPI
from profiles.router import router as profiles_router
from profiles.error_handlers import add_custom_exception_handlers

app = FastAPI()

app.include_router(profiles_router)
add_custom_exception_handlers(app)
