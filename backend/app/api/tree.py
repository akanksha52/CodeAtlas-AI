from fastapi import APIRouter, HTTPException
from app.core.dependencies import index_manager
from app.schemas.tree import FileNode, TreeResponse

router = APIRouter()


@router.get(
    "/tree",
    response_model=TreeResponse,
)
def get_tree():

    if not index_manager.ready():
        raise HTTPException(
            status_code=400,
            detail="Repository not indexed."
        )

    files = []

    for repository_file in index_manager.repository_index.files:

        files.append(
            FileNode(
                path=repository_file.path,
                language=repository_file.language.value,
            )
        )

    files.sort(key=lambda file: file.path)

    return TreeResponse(
                    repository=index_manager.repository_path,
                    total_files=len(files),
                    files=files,
                )