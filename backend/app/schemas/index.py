from pydantic import BaseModel


class IndexRequest(BaseModel):
    repository_path: str


class IndexResponse(BaseModel):
    success: bool
    files: int
    message: str