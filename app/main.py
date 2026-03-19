from fastapi import FastAPI
from app.agent import run_agent

app = FastAPI()


@app.get("/ask")
def ask(q: str):
    return {"response": run_agent(q)}