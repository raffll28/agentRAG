---
tags: [tecnologias, stack]
---

# Tecnologias — referência para o agente

## Linguagens de programação

- **Python**: dados, ML, automação, web (FastAPI, Django); ecossistema `uv`/`pip`.
- **JavaScript/TypeScript**: web front-end e Node.js; tipagem com TS reduz erros.
- **Rust**: segurança de memória e desempenho; sistemas e CLI.
- **Go**: concorrência simples; serviços em rede e CLIs.

## Web

- **HTML/CSS/JS**: base do browser.
- **Frameworks front**: React, Vue, Svelte.
- **Frameworks back**: FastAPI, Express, Spring.
- **HTTP/1.1 e HTTP/2**: multiplexação e compressão de cabeçalhos no HTTP/2 reduzem latência em sites com muitos recursos.
- **WebSockets**: canal full-duplex sobre TCP para apps em tempo real (chat, dashboards ao vivo).
- **GraphQL**: linguagem de consulta sobre uma API tipada; cliente pede só os campos necessários (boa para UIs flexíveis).

## Dados e persistência

- **SQL**: PostgreSQL, MySQL, SQLite — modelo relacional e ACID.
- **NoSQL**: MongoDB (documento), Redis (cache/fila), Elasticsearch (busca).

## Nuvem e infra como código

- **AWS, GCP, Azure**: compute (VM, serverless), storage, redes gerenciadas.
- **Terraform**: IaC declarativa para provisionar recursos.

## Formatos de dados e contratos

- **JSON**: troca ubíqua em APIs REST; legível e amplamente suportado.
- **YAML**: configuração legível (CI, Kubernetes, Ansible); cuidado com indentação.
- **Protobuf** / **gRPC**: serialização binária compacta; comum em microsserviços internos.

## Mobile e multiplataforma

- **Flutter** (Dart) e **React Native** (JS/TS): UIs nativas ou híbridas a partir de uma base de código; trade-offs de desempenho e ecossistema.

## Inteligência artificial

- **LLM**: modelos de linguagem; inferência local com **Ollama** ou serviços na nuvem.
- **RAG** (retrieval-augmented generation): recuperar trechos relevantes (ex.: Markdown em `app/memory/`) antes de gerar a resposta — padrão deste repositório (**agentRAG**).

## Infra de aplicação e desenho

- **Containers**: detalhes de Docker, Dockerfile e Compose — `docker-and-containers.md`.
- **Ollama** (inferência local, API, GPU): `ollama-local-inference.md`.
- **Arquitetura de software** (monólito, microsserviços, camadas, hexagonal, CQRS): `software-architecture-patterns.md`.

## Onde há exemplos (comandos e trechos)

- Vários arquivos `.md` nesta pasta incluem blocos curtos: `docker-and-containers.md`, `http-and-apis.md`, `ollama-local-inference.md`, `git-workflows.md`, `sql-databases.md`, `python-packaging-and-uv.md`, `linux-and-shell-basics.md`, `kubernetes-overview.md`, `rag-and-search-patterns.md`. O doc do próprio projeto: `python-fastapi-ollama.md` (curl na API).

## Mensageria e eventos

- **Kafka**, **RabbitMQ**: filas e streams para sistemas assíncronos e desacoplados.

## Observabilidade

- **Logs, métricas, traces**: OpenTelemetry; agregação com Prometheus/Grafana ou equivalentes na nuvem.
