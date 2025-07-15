from src.modules.context_update.dto import UpdateContextRequest, UpdateContextResponse
from src.core.llm import get_llm_response
import os

def _get_prompt_template() -> str:
    with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), "r", encoding="utf-8") as f:
        return f.read()

def update_context(request: UpdateContextRequest) -> UpdateContextResponse:
    # 플레이어 리스트를 문자열로 변환
    company_context_str = "\n".join([f"Day: {key} - Context: {value}" for key, value in request.company_context.items()])
    player_context_list_str = ""
    for player in request.player_context_list:
        player_context_str = "\n".join([f"Day: {key} - Context: {value}" for key, value in player.context.items()])
        player_context_list_str += f"player_id: {player['id']}, player_name: {player['name']}, player_role: {player['role']}, player_context: ({player_context_str})\n"
    
    
    agenda_list_str = "\n".join([f"{agenda.id}: {agenda.name} ({agenda.description})" + (f" - 선택: {', '.join([option.text for option in agenda.selected_options.values()])}" if agenda.selected_options else "") for agenda in request.agenda_list])
    
    # task_list는 dict[str, list[Task]] 형태이므로 각 리스트의 Task들을 처리
    task_list_str = "\n".join([f"{task.id}: {task.name} ({task.description})" + (f" - 선택: {task.selected_option.text}" if task.selected_option else "") for task_list in request.task_list.values() for task in task_list])
    
    # overtime_task_list는 dict[str, list[OvertimeTask]] 형태이므로 각 리스트의 OvertimeTask들을 처리
    overtime_task_list_str = "\n".join([f"{overtime_task.id}: {overtime_task.name} ({overtime_task.description})" + (f" - 선택: {overtime_task.selected_option.text}" if overtime_task.selected_option else "") for task_list in request.overtime_task_list.values() for overtime_task in task_list])
    
    # 프롬프트 템플릿 가져오기
    prompt_str = _get_prompt_template()
    
    # LLM 응답 받기
    response = get_llm_response(
        prompt_str=prompt_str,
        input_variables={"company_context": company_context_str, "player_context_list": player_context_list_str, "agenda_list": agenda_list_str, "task_list": task_list_str, "overtime_task_list": overtime_task_list_str},
        response_format=UpdateContextResponse,
    )
    
    return response