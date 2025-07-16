from src.modules.result.dto import ResultRequest, ResultResponse
from src.core.llm import get_llm_response
import os

def _get_prompt_template() -> str:
    with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), "r", encoding="utf-8") as f:
        return f.read()

def calculate_result(request: ResultRequest) -> ResultResponse:
    # 회사 컨텍스트를 문자열로 변환
    company_context_str = "\n".join([f"Day {key}: {value}" for key, value in request.company_context.items()])
    
    # 플레이어 컨텍스트를 문자열로 변환
    player_context_list_str = ""
    for player in request.player_context_list:
        player_context_str = "\n".join([f"Day {key}: {value}" for key, value in player.context.items()])
        player_context_list_str += f"player_id: {player.id}, player_name: {player.name}, player_role: {player.role}, player_context: ({player_context_str})\n"
    
    # 프롬프트 템플릿 가져오기
    prompt_str = _get_prompt_template()
    
    # LLM 응답 받기
    response = get_llm_response(
        prompt_str=prompt_str,
        input_variables={
            "company_context": company_context_str,
            "player_context_list": player_context_list_str
        },
        response_format=ResultResponse,
    )
    
    return response