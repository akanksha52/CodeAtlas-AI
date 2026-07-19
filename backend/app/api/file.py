from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.core.dependencies import index_manager
from app.schemas.file import FileResponse

router = APIRouter()


@router.get(
    "/file",
    response_model=FileResponse,
)
def get_file(path: str):

    if not index_manager.ready():
        raise HTTPException(
            status_code=400,
            detail="Repository not indexed.",
        )

    repository_path = Path(index_manager.repository_path)

    full_path = repository_path / path

    if not full_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found.",
        )

    return FileResponse(
        path=path,
        language=full_path.suffix.lstrip("."),
        content=full_path.read_text(
            encoding="utf-8"
        ),
    )