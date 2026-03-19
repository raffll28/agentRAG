# Normas do projeto (lembrete)

Documento curto para manter o fluxo de trabalho alinhado. Código e nomes de arquivos permanecem em **inglês**; esta referência está em **português**.

## Ambiente e dependências

- Use **apenas [uv](https://github.com/astral-sh/uv)** para ambiente e dependências neste repositório.
- Sincronizar deps: `uv sync` (inclui o grupo `dev` quando necessário: `uv sync --group dev`).
- Rodar comandos no contexto do projeto: `uv run <comando>` (ex.: `uv run pytest`, `uv run python run.py`).
- Evite `pip install` solto na raiz do projeto; alterações de dependência vão no `pyproject.toml` e no `uv.lock`.

## Testes antes de commit e push

- Antes de **commit** e **push**, execute: `uv run pytest`.
- Corrija falhas ou ajuste testes antes de enviar alterações.

## Git

- Mensagens de commit em **inglês**, no formato **Conventional Commits** (ex.: `feat(agent): add tool registry`).
- Escopo alinhado ao componente quando fizer sentido (ex.: `agent`, `tools`, `api`).

## Executar a API

- Servidor de desenvolvimento: `uv run python run.py` (FastAPI em `http://127.0.0.1:8000`, reload ativo).
- Endpoint principal: `GET /ask?q=...`.
- Variáveis do Ollama (opcional): copie `.env.example` para `.env` e ajuste `OLLAMA_URL`, `OLLAMA_MODEL`, `OLLAMA_TIMEOUT`.

## Memória do agente

- Arquivos de contexto do agente ficam em `app/memory/` (versionado; use `.gitkeep` ou arquivos reais conforme necessidade).
