from src.modules.context.dto import CreateContextRequest, CreateContextResponse
from src.core.llm import get_llm_response
import os

def _get_prompt_template() -> str:
    with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), "r", encoding="utf-8") as f:
        return f.read()

def create_context(request: CreateContextRequest) -> CreateContextResponse:
    # 플레이어 리스트를 문자열로 변환
    player_list_str = "\n".join([f"{player.id}: {player.name}" for player in request.player_list])
    
    # 프롬프트 템플릿 가져오기
    prompt_str = _get_prompt_template()
    
    # LLM 응답 받기
    response = get_llm_response(
        prompt_str=prompt_str,
        input_variables={"story": request.story, "player_list": player_list_str, "max_turn": request.max_turn},
        response_format=CreateContextResponse,
    )
    
    return response