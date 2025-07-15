from fastapi import APIRouter
from src.modules.context_update.service import update_context
from src.modules.context_update.dto import UpdateContextRequest, UpdateContextResponse

router = APIRouter()

@router.post("/context-update", response_model=UpdateContextResponse)
async def update_context_route(request: UpdateContextRequest) -> UpdateContextResponse:
    return update_context(request)