---
tags: [ollama, llm, inferencia-local, gpu]
---

# Ollama — inferência local de LLM

## O que é

- **Ollama** é um runtime que baixa e executa modelos de linguagem localmente, expondo uma **API HTTP** (porta padrão **11434**).
- Alternativa a chamar apenas APIs na nuvem: privacidade, custo previsível e offline após baixar pesos.

## CLI básica

- **`ollama pull <modelo>`**: baixa pesos (ex.: `llama3.2`, `ministral-3:14b`).
- **`ollama list`**: modelos instalados e tags exatas — usar o nome completo ao integrar apps.
- **`ollama run <modelo>`**: chat interativo no terminal.
- Tags frequentemente incluem **tamanho** ou **quantização** (ex.: `:7b`, variantes **Q4** mais leves).

Exemplo de uma linha no terminal:

```bash
ollama run llama3.2 "Say hello in one sentence."
```

## API HTTP

- **`POST /api/generate`**: geração com campo `prompt` e `model`; resposta JSON com `response` (modo não-stream).
- **`POST /api/chat`**: mensagens no estilo chat (roles `user` / `assistant`).
- **Streaming**: `stream: true` envia pedaços em NDJSON; clientes devem consumir a sequência.
- Integrações costumam apontar variável **`OLLAMA_URL`** para o endpoint de **generate** ou base; conferir documentação no cliente.

Exemplo com `curl` (substitua `my-model` por um nome retornado por `ollama list`):

```bash
curl -s http://localhost:11434/api/generate -d "{\"model\": \"my-model\", \"prompt\": \"Why is the sky blue?\", \"stream\": false}"
```

## GPU e desempenho

- **NVIDIA (CUDA)**, **AMD (ROCm)** e **Apple (Metal)** aceleram quando drivers e runtime estão corretos; sem GPU, **CPU** é possível porém lenta para modelos grandes.
- **VRAM** limita tamanho do modelo carregado; quantização (**Q4_K_M**, etc.) reduz uso e velocidade de inferência.
- **Context length** alto aumenta uso de memória; ajustar expectativas em hardware modesto.

## Modelfile

- **Modelfile** declara **FROM** um modelo base, **SYSTEM**, **PARAMETER** (temperatura, contexto), **TEMPLATE** — útil para personas e defaults sem alterar o app.

## Serviço Ollama

- Variáveis de ambiente do **daemon** Ollama (ex.: diretório de modelos, hosts) dependem da instalação; não confundir com o **`.env`** do aplicativo que consome a API.
- Atualizar Ollama e modelos para correções de segurança e desempenho.

## Boas práticas

- Um modelo por tarefa: modelos menores para classificação rápida; maiores para raciocínio pesado.
- Monitorar uso de VRAM e temperatura; throttling reduz throughput.
