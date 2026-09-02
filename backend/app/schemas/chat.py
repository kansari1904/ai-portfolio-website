from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question asked by the user.",
    )


class ChatResponse(BaseModel):
    route: str
    answer: str