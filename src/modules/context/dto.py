from pydantic import BaseModel

class Player(BaseModel):
    id: str
    name: str
    
class CreateContextRequest(BaseModel):
    max_turn: int
    story: str
    player_list: list[Player]           
    
class PlayerContext(BaseModel):
    id: str
    name: str
    role: str
    context: dict[str, str] # key: 일자, value: 플레이어 상태 설명

class CreateContextResponse(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]