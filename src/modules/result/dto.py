from pydantic import BaseModel
from typing import List

class PlayerContext(BaseModel):
    id: str
    name: str
    role: str
    context: dict[str, str] # key: 일자, value: 플레이어 상태 설명

class GameResult(BaseModel):
    success: bool
    summary: str

class PlayerRanking(BaseModel):
    rank: int
    id: str
    name: str
    role: str
    evaluation: str

class ResultRequest(BaseModel):
    company_context: dict[str, str]
    player_context_list: list[PlayerContext]

class ResultResponse(BaseModel):
    game_result: dict
    player_rankings: List[dict]