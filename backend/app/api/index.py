from fastapi import APIRouter, HTTPException
from app.schemas.index import (
    IndexRequest,
    IndexResponse,
)
from app.core.dependencies import index_manager

router = APIRouter()
@router.post(
    "/index",
    response_model=IndexResponse,
)

def build_index(request: IndexRequest):
    try:
        index_manager.build(
            request.repository_path
        )
        return IndexResponse(
            success=True,
            files=len(
                index_manager.repository_index.files
            ),
            message="Repository indexed successfully.",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )