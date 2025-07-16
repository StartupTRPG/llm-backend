from enum import Enum
from pydantic import BaseModel

class PlayerContext(BaseModel):
    id: str
    name: str
    role: str
    context: dict[str, str] # key: 일자, value: 플레이어 상태 설명
    
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
    
class CreateOvertimeRequest(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]
    
class CreateOvertimeResponse(BaseModel):
    task_list: dict[str, list[OvertimeTask]] # key: 플레이어 ID, value: 플레이어의 Overtime or Rest 리스트