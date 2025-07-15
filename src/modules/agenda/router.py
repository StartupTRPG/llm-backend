from fastapi import APIRouter
from src.modules.agenda.service import create_agenda
from src.modules.agenda.dto import CreateAgendaRequest, CreateAgendaResponse

router = APIRouter()

@router.post("/agenda", response_model=CreateAgendaResponse)
async def create_agenda_route(request: CreateAgendaRequest) -> CreateAgendaResponse:
    return create_agenda(request)