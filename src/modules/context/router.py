from fastapi import APIRouter
from src.modules.context.service import create_context
from src.modules.context.dto import CreateContextRequest, CreateContextResponse

router = APIRouter()

@router.post("/context", response_model=CreateContextResponse)
async def create_context_route(request: CreateContextRequest) -> CreateContextResponse:
    return create_context(request)