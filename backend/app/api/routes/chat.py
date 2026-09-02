from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest, ChatResponse

from app.services.chat_service import (
    process_question,
    stream_question,
)

from app.services.question_service import (
    FAQNotFoundError,
    get_faq_by_id,
    get_faq_suggestions,
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.get("/suggestions")
def get_chat_suggestions():
    return {
        "suggestions": get_faq_suggestions()
    }


@router.get("/faq/{faq_id}")
def get_faq(faq_id: str):
    try:
        return get_faq_by_id(faq_id)

    except FAQNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):
    try:
        result = process_question(
            request.question
        )

        return ChatResponse(
            route=result["route"],
            answer=result["answer"],
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.post("/stream")
def chat_stream(request: ChatRequest):
    try:
        return StreamingResponse(
            stream_question(request.question),
            media_type="text/plain",
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc