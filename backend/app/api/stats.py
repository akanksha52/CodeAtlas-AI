from fastapi import APIRouter, HTTPException

from app.core.dependencies import index_manager
from app.schemas.stats import StatsResponse

router = APIRouter()


@router.get(
    "/stats",
    response_model=StatsResponse,
)
def get_stats():

    if not index_manager.ready():
        raise HTTPException(
            status_code=400,
            detail="Repository not indexed."
        )

    repository = index_manager.repository_index

    files = len(repository.files)

    classes = 0
    functions = 0
    imports = 0

    for file in repository.files:
        for symbol in file.symbols:

            name = symbol.__class__.__name__

            if name == "FunctionSymbol":
                functions += 1

            elif name == "ClassSymbol":
                classes += 1

            elif name == "ImportSymbol":
                imports += 1

    return StatsResponse(
        repository=index_manager.repository_path,
        files=files,
        classes=classes,
        functions=functions,
        imports=imports,
        chunks=len(index_manager.chunks),
        embeddings=len(index_manager.chunks),
    )