from fastapi import APIRouter
from src.modules.task.service import create_task
from src.modules.task.dto import CreateTaskRequest, CreateTaskResponse

router = APIRouter()

@router.post("/task", response_model=CreateTaskResponse)
async def create_task_route(request: CreateTaskRequest) -> CreateTaskResponse:
    return create_task(request)