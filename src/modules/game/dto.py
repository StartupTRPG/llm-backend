from pydantic import BaseModel

class Player(BaseModel):
    id: str
    name: str
    
class GameRequest(BaseModel):
    player_list: list[Player]
    
class GameResponse(BaseModel):
    story: str