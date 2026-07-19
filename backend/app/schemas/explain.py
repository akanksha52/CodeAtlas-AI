from pydantic import BaseModel


class ExplainRequest(BaseModel):
    path: str


class ExplainResponse(BaseModel):
    explanation: str