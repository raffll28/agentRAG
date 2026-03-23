---
tags: [nosql, redis, mongodb, cache]
---

# NoSQL e cache

## Famílias NoSQL

- **Documento** (MongoDB, CouchDB): JSON aninhado; flexível para esquemas em evolução.
- **Chave-valor** (Redis, DynamoDB): leitura rápida por chave; TTL comum em caches.
- **Colunar** (Cassandra, Bigtable): analítico e escala horizontal massiva.
- **Grafo** (Neo4j): relações complexas e travessias.

## Onde usar

- **NoSQL** quando modelo de dados é variável ou escala horizontal é prioridade.
- **SQL** quando integridade relacional e relatórios ad-hoc são centrais.

## Redis

- **In-memory** com persistência opcional (RDB, AOF).
- Estruturas: strings, hashes, listas, sets, sorted sets, streams.
- **Pub/Sub** e **Streams** para mensageria leve; cuidado com perda de mensagens em memória pura.

## Cache

- **Cache-aside**: app lê cache, em miss busca DB e popula.
- **TTL** e **invalidação** evitam dados obsoletos; **cache stampede** pode exigir locks ou single-flight.
- **CDN** cacheia conteúdo estático próximo ao usuário.

## Boas práticas

- Definir limites de memória e política de eviction (**LRU** comum).
- Não armazenar segredos só em cache sem proteção.
