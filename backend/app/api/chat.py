from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.index_manager import IndexManager
from app.services.rag_service import RAGService

router = APIRouter()

index_manager = IndexManager()
if not index_manager.ready():
    index_manager.build("sample_repo")

rag_service = RAGService(index_manager)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response = rag_service.ask(request.message)

        return ChatResponse(
            response=response
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )