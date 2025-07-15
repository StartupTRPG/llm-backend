from fastapi import APIRouter
from src.modules.overtime.service import create_overtime
from src.modules.overtime.dto import CreateOvertimeRequest, CreateOvertimeResponse

router = APIRouter()

@router.post("/overtime", response_model=CreateOvertimeResponse)
async def create_overtime_route(request: CreateOvertimeRequest) -> CreateOvertimeResponse:
    return create_overtime(request)