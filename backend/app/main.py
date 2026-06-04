from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.user import router as user_router
from app.api.v1.word import router as word_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(word_router)