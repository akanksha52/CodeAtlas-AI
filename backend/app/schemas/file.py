from pydantic import BaseModel


class FileRequest(BaseModel):
    path: str


class FileResponse(BaseModel):
    path: str
    language: str
    content: str