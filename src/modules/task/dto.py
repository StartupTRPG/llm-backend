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
    options: list[TaskOption]
    
class CreateTaskRequest(BaseModel):
    company_context: dict[str, str] # key: 일자, value: 회사 상태 설명
    player_context_list: list[PlayerContext]
    
class CreateTaskResponse(BaseModel):
    task_list: dict[str, list[Task]] # key: 플레이어 ID, value: 플레이어의 업무 리스트