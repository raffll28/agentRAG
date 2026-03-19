# agentRAG

FastAPI service that runs a small tool-using agent backed by a local [Ollama](https://ollama.com/) model.

## Quick start

```bash
uv sync --group dev
cp .env.example .env   # optional; edit Ollama URL/model
uv run python run.py
```

Open `http://127.0.0.1:8000/ask?q=your+question` (Ollama must be running).

## Project notes

- Conventions and workflow: see [PROJECT_NORMS.md](PROJECT_NORMS.md).
- Agent memory files live under `app/memory/`.
