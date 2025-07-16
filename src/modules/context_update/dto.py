from enum import Enum
from pydantic import BaseModel

class PlayerContext(BaseModel):
    id: str
    name: str
    role: str
    context: dict[str, str] # key: 일자, value: 플레이어 상태 설명
    
class TaskOption(BaseModel):
    id: str
    text: str
    impact_summary: str

class Task(BaseModel):
    id: str
    name: str
    description: str
    selected_option: TaskOption

class AgendaOption(BaseModel):
    id: str
    text: str
    impact_summary: str
    
class Agenda(BaseModel):
    id: str
    name: str
    description: str
    selected_options: dict[str, AgendaOption] # key: player_id, value: 선택된 안건 옵션
    
class OvertimeTaskType(Enum):
    OVERTIME = "overtime"
    REST = "rest"

class OvertimeTaskOption(BaseModel):
    id: str
    text: str
    impact_summary: str
    
class OvertimeTask(BaseModel):
    id: str
    type: OvertimeTaskType
    name: str
    description: str
    options: list[OvertimeTaskOption]
    selected_option: OvertimeTaskOption
    

class UpdateContextRequest(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]
    
    agenda_list: list[Agenda]
    task_list: dict[str, list[Task]]
    overtime_task_list: dict[str, list[OvertimeTask]]

# 플레이어 선택에 따라 회사 상태 설명, 플레이어 상태 설명, 안건, 업무, 야근 업무 조정
class UpdateContextResponse(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]