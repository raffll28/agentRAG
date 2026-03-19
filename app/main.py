import asyncio
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.agent import run_agent
from app.settings import get_settings

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

app = FastAPI()

_agent_sem = asyncio.Semaphore(get_settings().agent_max_concurrent)


class AskBody(BaseModel):
    q: str = Field(min_length=1, max_length=32000)


@app.get("/ask")
async def ask_get(q: str):
    async with _agent_sem:
        response = await asyncio.to_thread(run_agent, q)
    return {"response": response}


@app.post("/ask")
async def ask_post(body: AskBody):
    async with _agent_sem:
        response = await asyncio.to_thread(run_agent, body.q)
    return {"response": response}


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
