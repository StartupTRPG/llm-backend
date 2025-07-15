from fastapi import APIRouter
from src.modules.game.service import create_game
from src.modules.game.dto import GameRequest, GameResponse

router = APIRouter()

@router.post("/game", response_model=GameResponse)
async def create_game_route(request: GameRequest) -> GameResponse:
    return create_game(request)