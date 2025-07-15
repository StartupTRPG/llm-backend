from fastapi import FastAPI, Request
import uvicorn
from src.modules.game.router import router as game_router
from src.modules.context.router import router as context_router
from src.modules.task.router import router as task_router
from src.modules.overtime.router import router as overtime_router
from src.modules.context_update.router import router as context_update_router
from src.modules.agenda.router import router as agenda_router
from src.modules.explanation.router import router as explanation_router
from src.modules.result.router import router as result_router
import logging

app = FastAPI()
app.include_router(game_router)
app.include_router(context_router)
app.include_router(agenda_router)
app.include_router(task_router)
app.include_router(overtime_router)
app.include_router(context_update_router)
app.include_router(explanation_router)
app.include_router(result_router)



# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_request_middleware(request: Request, call_next):
    logger.info(f"요청: {request.method} {request.url}")
    response = await call_next(request)
    return response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )