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
    agenda_option_id: str
    agenda_option_text: str
    agenda_option_impact_summary: str
    
class Agenda(BaseModel):
    agenda_id: str
    agenda_name: str
    agenda_description: str
    agenda_options: list[AgendaOption]
    
class CreateAgendaResponse(BaseModel):
    description: str
    agenda_list: list[Agenda]