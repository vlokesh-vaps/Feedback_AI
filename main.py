from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from pathlib import Path

from app import get_ai_response

app = FastAPI(title="Feedback Assistant API", version="1.0.0")
UI_FILE = Path(__file__).parent / "ui" / "index.html"


class ChatRequest(BaseModel):
    message: str
    history: list[dict[str, str]] = Field(default_factory=list)


@app.get("/health")
async def health_check():
    return {"success": True, "status": "ok"}


@app.get("/")
async def ui():
    return FileResponse(UI_FILE)


@app.post("/chat")
async def chat(request: ChatRequest):
    ai_reply = get_ai_response(request.message, request.history)
    return {"success": True, "reply": ai_reply}
