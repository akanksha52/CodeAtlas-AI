from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.index_manager import IndexManager
from app.services.rag_service import RAGService
from app.core.dependencies import index_manager

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        rag_service = RAGService(index_manager)
        response = rag_service.ask(request.message)

        return ChatResponse(
            response=response
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )