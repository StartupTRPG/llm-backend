from fastapi import APIRouter
from src.modules.result.dto import ResultRequest, ResultResponse
from src.modules.result.service import calculate_result

router = APIRouter(prefix="/result")

@router.post("/", response_model=ResultResponse)
async def calculate_result_route(request: ResultRequest):
    return calculate_result(request)