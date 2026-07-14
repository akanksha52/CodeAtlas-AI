from fastapi import APIRouter, HTTPException
from app.services.chat_service import ChatService
from app.core.config import settings
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.exception import LLMServiceError

router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)

chat_service=ChatService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response = chat_service.chat(request.message)
        return ChatResponse(
            response=response
        )
    except LLMServiceError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e)
        )