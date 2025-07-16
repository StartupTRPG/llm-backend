from pydantic import BaseModel

class PlayerContext(BaseModel):
    id: str
    name: str
    role: str
    context: dict[str, str] # key: 일자, value: 플레이어 상태 설명

class ExplanationRequest(BaseModel):
    company_context: dict[str, str]
    player_context_list: list[PlayerContext]

class ExplanationResponse(BaseModel):
    explanation: str