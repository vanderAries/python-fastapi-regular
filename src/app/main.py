from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
