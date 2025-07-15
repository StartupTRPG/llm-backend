from pydantic import BaseModel


class ExplanationRequest(BaseModel):
    company_context: dict
    player_context_list: list[dict]

class ExplanationResponse(BaseModel):
    explanation: str