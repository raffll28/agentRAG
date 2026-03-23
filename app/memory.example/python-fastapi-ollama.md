---
tags: [python, fastapi, ollama, este-projeto]
---

> Os ficheiros em `app/memory.example/` são o template versionado no Git; após um clone, copie-os para `app/memory/` (ver README e PROJECT_NORMS).

# Stack deste repositório (agentRAG)

## Componentes

- **FastAPI**: framework web assíncrono; expõe `GET /ask` com parâmetro de consulta.
- **Uvicorn**: servidor ASGI usado em desenvolvimento via `run.py`.
- **Ollama**: API HTTP local em `localhost:11434` para inferência de modelos (ex.: Ministral / família Mistral).
- **uv**: gerenciador de ambiente e dependências Python; usar `uv sync` e `uv run`.

Conceitos gerais do Ollama (CLI, API, GPU, Modelfile): ver **`ollama-local-inference.md`** nesta pasta.

## Memória do agente

- Arquivos em `app/memory/` são lidos pelas tools `list_files`, `read_file`, `grep_memory`, buscas por substring (`search_memory`, `search_memory_all_terms`) e buscas ranqueadas por **BM25** (`search_memory_bm25`, `search_memory_all_terms_bm25` — última exige que todos os termos apareçam no texto, como na variante sem BM25).
- Use substring quando a frase exata importa; use BM25 para ranquear por relevância léxica (termos soltos, sem exigir a substring contígua da query inteira).
- Formato recomendado: **Markdown** (`.md`) com seções claras para leitura e busca textual.

## Variáveis de ambiente (LLM)

Crie o arquivo **`.env`** na raiz do repositório copiando **`.env.example`** e preencha os valores. O `.env` não é versionado; cada ambiente escolhe o modelo instalado no Ollama.

- `OLLAMA_URL`: endpoint de geração (padrão no código: `http://localhost:11434/api/generate`).
- `OLLAMA_MODEL`: **obrigatório** — nome exato do modelo no Ollama (`ollama list`); não há valor padrão no código.
- `OLLAMA_TIMEOUT`: timeout da requisição em segundos (opcional; padrão no código: `120`).

## Limites de memória e escala (opcional)

Variáveis como `MEMORY_SEARCH_MAX_TOTAL_CHARS`, `MEMORY_MAX_BYTES_PER_FILE_SEARCH`, `AGENT_MAX_CONCURRENT` e `READ_FILE_MAX_CHARS` controlam tamanho de buscas e carga do agente — ver `.env.example` na raiz do repositório.

## Testar a API (servidor em execução)

Com `uv run python run.py` e Ollama configurado, exemplos com `curl`:

```bash
curl -sS "http://127.0.0.1:8000/ask?q=hello"
curl -sS -X POST "http://127.0.0.1:8000/ask" -H "Content-Type: application/json" -d "{\"q\":\"hello\"}"
```
