from pydantic import BaseModel

class PlayerContext(BaseModel):
    id: str
    name: str
    role: str
    context: dict[str, str] # key: 일자, value: 플레이어 상태 설명
    
class CreateAgendaRequest(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]
    
class AgendaOption(BaseModel):
    id: str
    text: str
    impact_summary: str
    
class Agenda(BaseModel):
    id: str
    name: str
    description: str
    options: list[AgendaOption]
    
class CreateAgendaResponse(BaseModel):
    description: str
    agenda_list: list[Agenda]