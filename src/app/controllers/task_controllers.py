import uuid
from datetime import datetime

from app.models.tasks import TaskModel, TaskRequest
from app.models.errors import ErrorResponse


def create_task(task: TaskRequest) -> TaskModel | ErrorResponse:
    try:
        new_task = TaskModel(
            id=str(uuid.uuid4()),
            name=task.name,
            description=task.description,
            category=task.category,
            state=task.state,
            createdAt=str(datetime.now().timestamp()),
            updatedAt=str(datetime.now().timestamp()),
        )
        return new_task
    except ValidationError as error:
        error_res = ErrorResponse(
            title="Validation Error",
            detail="Provided request body is invalid, check 'errors' for more info.",
            errors=error.errors(),
        )
        # If validation fails, you can handle it and return a custom error response
        raise HTTPException(status_code=400, detail=error_res) from error
