from fastapi import APIRouter
from src.modules.explanation.service import create_explanation
from src.modules.explanation.dto import ExplanationRequest, ExplanationResponse

router = APIRouter()

@router.post("/explanation", response_model=ExplanationResponse)
async def create_explanation_route(request: ExplanationRequest) -> ExplanationResponse:
    return create_explanation(request)