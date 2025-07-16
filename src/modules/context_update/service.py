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
        player_context_list_str += f"player_id: {player.id}, player_name: {player.name}, player_role: {player.role}, player_context: ({player_context_str})\n"
    
    # agenda_list를 딕셔너리로 처리
    agenda_list_str = ""
    for agenda in request.agenda_list:
        agenda_id = agenda.get('id', '')
        agenda_name = agenda.get('name', '')
        agenda_description = agenda.get('description', '')
        selected_options = agenda.get('selected_options', {})
        
        selected_texts = []
        for option in selected_options.values():
            if isinstance(option, dict):
                selected_texts.append(option.get('text', ''))
            else:
                selected_texts.append(option.text if hasattr(option, 'text') else '')
        
        agenda_list_str += f"{agenda_id}: {agenda_name} ({agenda_description})"
        if selected_texts:
            agenda_list_str += f" - 선택: {', '.join(selected_texts)}"
        agenda_list_str += "\n"
    
    # task_list를 딕셔너리로 처리
    task_list_str = ""
    for player_id, task_list in request.task_list.items():
        for task in task_list:
            task_id = task.get('id', '')
            task_name = task.get('name', '')
            task_description = task.get('description', '')
            selected_option = task.get('selected_option')
            
            task_list_str += f"{task_id}: {task_name} ({task_description})"
            if selected_option:
                if isinstance(selected_option, dict):
                    task_list_str += f" - 선택: {selected_option.get('text', '')}"
                else:
                    task_list_str += f" - 선택: {selected_option.text if hasattr(selected_option, 'text') else ''}"
            task_list_str += "\n"
    
    # overtime_task_list를 딕셔너리로 처리
    overtime_task_list_str = ""
    for player_id, overtime_task_list in request.overtime_task_list.items():
        for overtime_task in overtime_task_list:
            overtime_task_id = overtime_task.get('id', '')
            overtime_task_name = overtime_task.get('name', '')
            overtime_task_description = overtime_task.get('description', '')
            selected_option = overtime_task.get('selected_option')
            
            overtime_task_list_str += f"{overtime_task_id}: {overtime_task_name} ({overtime_task_description})"
            if selected_option:
                if isinstance(selected_option, dict):
                    overtime_task_list_str += f" - 선택: {selected_option.get('text', '')}"
                else:
                    overtime_task_list_str += f" - 선택: {selected_option.text if hasattr(selected_option, 'text') else ''}"
            overtime_task_list_str += "\n"
    
    # 프롬프트 템플릿 가져오기
    prompt_str = _get_prompt_template()
    
    # LLM 응답 받기
    response = get_llm_response(
        prompt_str=prompt_str,
        input_variables={"company_context": company_context_str, "player_context_list": player_context_list_str, "agenda_list": agenda_list_str, "task_list": task_list_str, "overtime_task_list": overtime_task_list_str},
        response_format=UpdateContextResponse,
    )
    
    return response