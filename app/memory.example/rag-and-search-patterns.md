---
tags: [rag, busca, bm25, agente]
---

# RAG e padrões de busca na memória

## O que é RAG

- **Retrieval-Augmented Generation**: recuperar trechos relevantes de fontes (aqui, Markdown em `app/memory/`) antes de o modelo responder, reduzindo alucinação e ancorando fatos.

## Ferramentas deste projeto

- **Substring**: `search_memory` exige a string (case-insensitive) no arquivo; `search_memory_all_terms` exige **todas** as palavras como substring.
- **BM25**: `search_memory_bm25` ranqueia arquivos por relevância léxica (bag-of-words); `search_memory_all_terms_bm25` combina pré-filtro de todos os termos com BM25.
- **grep_memory**: regex por linha para padrões precisos.

## Quando usar o quê

- Frase exata ou citação: **substring** ou **grep**.
- Consulta por palavras-chave soltas e ordem irrelevante: **BM25**.
- Estrutura de arquivo: **memory_toc** em `.md` com headings.

Formato de chamada de tool no agente (ilustrativo):

```text
Pensamento: preciso achar notas sobre TLS e HTTPS com ranqueamento.
Ação: search_memory_bm25
Entrada: tls https
```

## Boas práticas de autoria

- Títulos **`#` / `##`** claros; listas e termos consistentes melhoram busca e leitura humana.
- Evitar um único arquivo gigante; **vários arquivos temáticos** melhoram recall.
- Frontmatter **`tags`** ajuda contexto humano; busca textual usa o corpo do arquivo.

## Limites

- Variáveis **`MEMORY_*`** e **`READ_FILE_MAX_CHARS`** no `.env` limitam tamanho de leitura e saída — ver `.env.example`.
