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

### Reescrever histórico (remover `app/memory/` dos commits antigos)

**Aviso:** altera todos os SHAs; exige `git push --force-with-lease` e acordo com forks e colaboradores. Faça backup antes (ex.: `git clone --mirror <url> backup.git` ou cópia do diretório do repositório).

Só faz sentido **depois** de existir um commit que já coloca os templates em `app/memory.example/` e ignora `app/memory/*` (exceto `.gitkeep`), para não perder o conteúdo dos exemplos no histórico.

1. Instalar [git-filter-repo](https://github.com/newren/git-filter-repo) (substituto recomendado de `git filter-branch`).
2. Num clone de segurança ou após backup local: `git filter-repo --path app/memory/ --invert-paths` — remove **todo** o caminho `app/memory/` de **todo** o histórico (incluindo `.gitkeep` nos commits reescritos).
3. Se `app/memory/` deixar de existir no `HEAD`, recrie só o marcador: `app/memory/.gitkeep` vazio, `git add` e um commit (ex.: `chore(memory): add .gitkeep after filter-repo`).
4. O `filter-repo` pode remover a configuração do remoto; volte a registar: `git remote add origin <url>`.
5. Envio: `git push --force-with-lease origin main` (ajuste o nome do branch).

Forks e PRs podem precisar de rebase. Se alguma vez existiram segredos em ficheiros sob `app/memory/`, considere rotação de credenciais.

## Executar a API

- Servidor de desenvolvimento: `uv run python run.py` (FastAPI em `http://127.0.0.1:8000`, reload ativo).
- Interface de chat: abra `http://127.0.0.1:8000/` no navegador.
- API: `GET /ask?q=...` ou `POST /ask` com JSON `{"q":"..."}`.
- **Configuração local**: copie `.env.example` para `.env` na raiz do projeto. O arquivo **`.env` não é versionado** (gitignore); cada máquina define o próprio modelo e URLs.
- Ollama: **`OLLAMA_MODEL` é obrigatório** no `.env` (nome exato do modelo varia por ambiente; não há default no código). Opcionais: `OLLAMA_URL`, `OLLAMA_TIMEOUT`.
- Limites de escala (opcional): `AGENT_MAX_CONCURRENT`, `AGENT_MAX_PROMPT_CHARS`, `READ_FILE_MAX_CHARS`, `MEMORY_*` — ver `.env.example`.
- Produção: preferir `uvicorn` com vários workers (ver docstring em `run.py`), não apenas `reload=True`.

## Memória do agente

- Arquivos de contexto do agente ficam em `app/memory/` (local por máquina; não vão para o Git). O repositório mantém templates em `app/memory.example/` (Markdown). Após um clone, copie `app/memory.example/*.md` para `app/memory/` (Unix: `cp app/memory.example/*.md app/memory/`; PowerShell: `Copy-Item app/memory.example/*.md app/memory/`). Só `app/memory/.gitkeep` permanece versionado para a pasta existir vazia.
