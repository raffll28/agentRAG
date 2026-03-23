---
tags: [docker, containers, oci, dockerfile, compose]
---

# Docker e containers

## Conceitos

- **Imagem**: camadas somente leitura com filesystem e metadados; **container** é instância executável.
- **Dockerfile** descreve build em etapas; **multi-stage builds** reduzem tamanho final.
- **OCI** padroniza formato de imagem e runtime.

## Dockerfile — instruções comuns

- **FROM**: imagem base (pin por tag ou **digest** em produção).
- **WORKDIR**: diretório de trabalho para instruções seguintes.
- **COPY** vs **ADD**: preferir **COPY** para arquivos locais previsíveis; **ADD** tem semântica extra (URLs, tar auto-extract).
- **RUN**: executa comandos e cria nova camada; agrupar comandos com `&&` e limpar cache no mesmo **RUN** reduz tamanho.
- **CMD**: comando padrão do container (substituível por `docker run ...`).
- **ENTRYPOINT**: executável fixo; combina com `CMD` como argumentos padrão.
- **ARG** (build-time) vs **ENV** (runtime): segredos não devem ficar em **ARG** em builds públicos.

## Cache de layers

- Ordem importa: copiar primeiro **dependências** que mudam pouco (`package.json`, `requirements.txt`), depois o código-fonte, maximiza cache de **RUN** de instalação.
- **BuildKit** (padrão em versões recentes) melhora cache e paralelismo.

## Build avançado

- **BuildKit**: `DOCKER_BUILDKIT=1` ou habilitado por padrão.
- **buildx**: imagens **multi-arquitetura** (amd64/arm64) para laptops Apple e servidores mistos.
- **Build args**: `--build-arg` injeta valores no build sem gravá-los no Dockerfile versionado quando combinado com CI.

## Runtime

- **`docker run`**: flags comuns `--rm` (remove ao sair), `--init` (PID 1 leve), `-p` (portas), `-e` / `--env-file`.
- **Compose** orquestra vários serviços com rede e volumes nomeados; mesmo projeto, múltiplos containers.

Dockerfile mínimo (imagem que imprime versão do Python):

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "http.server", "8000"]
```

Build e execução com porta e variável:

```bash
docker build -t myapp:1.0 .
docker run --rm -p 8000:8000 -e PORT=8000 myapp:1.0
```

Dois serviços em Compose (esboço):

```yaml
services:
  web:
    image: nginx:alpine
    ports: ["8080:80"]
  api:
    image: myapp:1.0
    environment:
      NODE_ENV: production
```

## Rede e volumes

- **Bridge** (padrão), **host**, **overlay** (Swarm/Kubernetes).
- **Volumes** persistem dados fora do container; **bind mounts** ligam diretórios do host.

## Registries

- **Docker Hub**, **GHCR** (GitHub Container Registry), ECR/GCR na nuvem.
- Referência imutável por **digest** (`sha256:...`) evita surpresas quando a tag move.

## Segurança

- Rodar processos como **usuário não-root** (`USER` no Dockerfile ou `--user`).
- Não colocar **segredos** em layers: usar **secrets** do orchestrator, **BuildKit secrets**, ou montagens em runtime.
- Varredura de imagens (**Trivy**, **Grype**, scanners do registry) para CVEs em pacotes da imagem.

## Boas práticas

- **.dockerignore** exclui `node_modules`, `.git`, artefatos locais do contexto de build.
- **Tags** imutáveis (`sha` ou semver) para produção; evitar só `latest` em deploy.
- **Healthchecks** no Dockerfile para orquestradores reiniciarem instâveis.

## Limites

- **CPU/mem** via orchestrator ou `docker run --cpus` / `--memory`.

## Compose

- **docker-compose** (Compose file v2/v3) orquestra vários serviços locais ou de staging.
- Variáveis via **`.env`** ao lado do compose; não commitar segredos.

## Ollama e GPU

- **Ollama** para inferência local costuma rodar no **host** (acesso direto a GPU) ou em imagem oficial com drivers NVIDIA/ROCm corretos; containers sem GPU exposta caem em **CPU**, muito mais lento para LLMs.
