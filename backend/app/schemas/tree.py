from pydantic import BaseModel


class FileNode(BaseModel):
    path: str
    language: str


class TreeResponse(BaseModel):
    files: list[FileNode]