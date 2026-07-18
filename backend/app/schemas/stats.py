from pydantic import BaseModel


class StatsResponse(BaseModel):
    repository: str
    files: int
    classes: int
    functions: int
    imports: int
    chunks: int
    embeddings: int