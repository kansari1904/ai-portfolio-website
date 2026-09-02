from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.core.config import settings
from app.api.routes.chat import router as chat_router


app = FastAPI(
    title=settings.app_name,
    description="AI-powered recruiter portfolio assistant",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    health_router,
    prefix="/api",
)

app.include_router(
    chat_router,
    prefix="/api",
)


@app.get("/")
def root():
    return {
        "message": "AI Portfolio API is running"
    }