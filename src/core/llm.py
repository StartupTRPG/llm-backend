
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from src.core.config import settings
from pydantic import BaseModel
from typing import Optional, Type
import time
import json

_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.5,
    max_output_tokens=20000,
    google_api_key=settings.GEMINI_API_KEY
)
    
def get_llm_response(
    prompt_str: str,
    input_variables: dict,
    response_format: Optional[Type[BaseModel]] = None,
    max_retries: int = 5,
    retry_delay: float = 0.5,
):    

    # 프롬프트 템플릿 생성
    if response_format:
        format_instructions = f"""
다음 JSON 스키마에 따라 응답하세요:
{response_format.model_json_schema()}

JSON 객체만 응답하고 다른 텍스트는 포함하지 마세요.
"""
        full_prompt_str = prompt_str + "\n\n{format_instructions}"
        prompt = PromptTemplate(
            input_variables=list(input_variables.keys()) + ["format_instructions"],
            template=full_prompt_str
        )
        input_vars = {**input_variables, "format_instructions": format_instructions}
    else:
        prompt = PromptTemplate(
            input_variables=list(input_variables.keys()),
            template=prompt_str
        )
        input_vars = input_variables
    
    # 재시도 로직
    last_exception = None
    for attempt in range(max_retries):
        try:
            
            # LLM 응답 받기
            response = _llm.invoke(prompt.format(**input_vars))
            
            # 디버깅: 응답 내용 출력
            print(f"LLM 응답: {response.content}")
            print(f"응답 타입: {type(response.content)}")
            
            if response_format:
                # JSON 문자열을 파싱하고 Pydantic 모델로 변환
                if isinstance(response.content, str):
                    # 빈 문자열이나 None 체크
                    if not response.content or response.content.strip() == "":
                        raise ValueError("LLM이 빈 응답을 반환했습니다")
                    
                    # 코드 블록 제거 (```json ... ```)
                    content = response.content.strip()
                    if content.startswith("```json"):
                        content = content[7:]  # "```json" 제거
                    if content.endswith("```"):
                        content = content[:-3]  # "```" 제거
                    content = content.strip()
                    
                    try:
                        json_data = json.loads(content)
                    except json.JSONDecodeError as e:
                        print(f"JSON 파싱 실패: {content}")
                        raise ValueError(f"LLM 응답이 유효한 JSON이 아닙니다: {e}")
                else:
                    json_data = response.content
                
                # Pydantic V2 모델로 변환
                return response_format.model_validate(json_data)
            else:
                return response.content
                
        except Exception as e:
            last_exception = e
            if attempt < max_retries - 1:  # 마지막 시도가 아니면 재시도
                print(f"파싱 실패 (시도 {attempt + 1}/{max_retries}): {str(e)}")
                time.sleep(retry_delay)
            else:
                print(f"최대 재시도 횟수 초과. 마지막 오류: {str(e)}")
                raise last_exception
    
    # 이 부분은 실행되지 않지만 타입 안전성을 위해 추가
    raise last_exception
