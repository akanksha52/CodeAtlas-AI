from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class Source(BaseModel):
    file: str
    symbol: str
    type: str


class ChatResponse(BaseModel):
    response: str
    sources: list[Source]