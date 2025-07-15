from pydantic import BaseModel
from typing import List

class GameResult(BaseModel):
    success: bool
    summary: str

class PlayerRanking(BaseModel):
    rank: int
    player_id: str
    player_name: str
    player_role: str
    player_evaluation: str

class ResultRequest(BaseModel):
    company_context: dict[str, str]
    player_context_list: list[dict]

class ResultResponse(BaseModel):
    game_result: GameResult
    player_rankings: List[PlayerRanking]