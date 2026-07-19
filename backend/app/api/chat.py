from fastapi import APIRouter, HTTPException

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

from app.services.rag_service import RAGService
from app.core.dependencies import index_manager

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    #try:

    rag_service = RAGService(
            index_manager
        )

    result = rag_service.ask(
            request.message
        )

    return ChatResponse(**result)

    # except Exception as e:

    #     raise HTTPException(
    #         status_code=500,
    #         detail=str(e),
    #     )