from fastapi import APIRouter, HTTPException

from app.schemas.explain import (
    ExplainRequest,
    ExplainResponse,
)
from app.services.explain_service import ExplainService

router = APIRouter()

service = ExplainService()


@router.post(
    "/explain-file",
    response_model=ExplainResponse,
)
def explain_file(request: ExplainRequest):

    try:

        explanation = service.explain(
            request.path
        )

        return ExplainResponse(
            explanation=explanation
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )