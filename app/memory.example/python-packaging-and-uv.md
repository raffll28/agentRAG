---
tags: [python, uv, packaging, pyproject]
---

# Python: empacotamento e uv

## pyproject.toml

- Padrão moderno (**PEP 621**) para metadados do projeto e dependências.
- **Hatchling**, **setuptools**, **poetry-core** como backends de build.

## uv neste repositório

- **uv** gerencia ambiente e lockfile **`uv.lock`** (reproduzível).
- Comandos típicos: `uv sync` (instalar deps), `uv run <cmd>` (executar no ambiente do projeto).
- Grupos opcionais: `uv sync --group dev` para dependências de desenvolvimento.

Fluxo típico do projeto **agentRAG** (na raiz do clone):

```bash
uv sync --group dev
uv run pytest
uv run python run.py
```

## Ambientes virtuais

- `.venv/` local evita poluir Python global; IDEs apontam o interpretador para `.venv`.

## Publicação

- **Twine** envia pacotes ao **PyPI**; **version** em `pyproject.toml` segue semver.
- **Wheel** (`.whl`) é formato binário preferido; **sdist** para fonte.

## Boas práticas

- Fixar versões no lock; ranges semânticos no `pyproject` com cuidado.
- **Tipagem** gradual (`typing`, `TypedDict`) melhora manutenção.
- Evitar `pip install` solto na raiz quando o projeto padroniza **uv** (ver normas do repositório).
