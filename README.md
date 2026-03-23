# agentRAG

FastAPI service that runs a small tool-using agent backed by a local [Ollama](https://ollama.com/) model.

## Quick start

```bash
uv sync --group dev
cp .env.example .env
# Edit .env: set OLLAMA_MODEL (required) to the exact name from `ollama list`
# Copy agent memory templates into your local app/memory/ (not tracked by Git):
#   Unix: cp app/memory.example/*.md app/memory/
#   PowerShell: Copy-Item app/memory.example/*.md app/memory/
uv run python run.py
```

- Chat UI: `http://127.0.0.1:8000/`
- API: `GET` or `POST /ask` with query/body `q` (Ollama must be running).

## Configuration

Environment-specific settings live in **`.env`** (not committed; copy from [`.env.example`](.env.example)).

| Variable | Required | Notes |
|----------|----------|--------|
| `OLLAMA_MODEL` | **Yes** | Exact model tag from `ollama list`. No default in application code. |
| `OLLAMA_URL` | No | Defaults to `http://localhost:11434/api/generate`. |
| `OLLAMA_TIMEOUT` | No | Request timeout in seconds (default in code: `120`). |

Optional scalability limits (`AGENT_MAX_CONCURRENT`, `AGENT_MAX_PROMPT_CHARS`, `MEMORY_*`, `READ_FILE_MAX_CHARS`, etc.) are documented in `.env.example`.

## Project notes

- Conventions and workflow: see [PROJECT_NORMS.md](PROJECT_NORMS.md).
- Agent memory files live under `app/memory/` (per-machine; not committed). After clone, copy `app/memory.example/*.md` into `app/memory/` (see Quick start).
- Memory search: `search_memory` / `search_memory_all_terms` match substrings; `search_memory_bm25` / `search_memory_all_terms_bm25` rank files with BM25 (bag-of-words, one file = one document). Same env limits apply (`MEMORY_*` in `.env.example`).
