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
    overtime_task_option_id: str
    overtime_task_option_text: str
    overtime_task_option_impact_summary: str
    
class OvertimeTask(BaseModel):
    overtime_task_id: str
    overtime_task_type: OvertimeTaskType
    overtime_task_name: str
    overtime_task_description: str
    overtime_task_options: list[OvertimeTaskOption]
    
class CreateOvertimeRequest(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]
    
class CreateOvertimeResponse(BaseModel):
    task_list: dict[str, list[OvertimeTask]] # key: 플레이어 ID, value: 플레이어의 Overtime or Rest 리스트