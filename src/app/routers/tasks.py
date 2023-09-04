from fastapi import APIRouter, HTTPException, Response, status
from pydantic import ValidationError

from app.controllers import task_controllers

from app.models.tasks import TaskModel, TaskRequest
from app.models.errors import ErrorResponse

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED) # or maybe use response_model instead of "->"
def create_task(task: TaskRequest) -> TaskModel | ErrorResponse:
    # Validation error here or in controllers? maybe add validation middleware??
    return task_controllers.create_task(task)


@router.get("/")
def get_all_tasks() -> list[TaskModel] | ErrorResponse:
    return [{"id": "1"}, {"id": "2"}]


@router.get("/{task_id}")
def get_task_by_id(task_id: str) -> TaskModel | ErrorResponse:
    return {"task": task_id}


@router.put("/{task_id}")
def update_task(task_id: str, task: TaskRequest) -> TaskModel | ErrorResponse:
    return {"task": task_id}


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_task(task_id: str) -> None:
    print(task_id)

