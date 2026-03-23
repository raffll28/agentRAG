---
tags: [http, rest, api, web]
---

# HTTP e APIs

## Métodos HTTP

- **GET**: leitura idempotente; não deve ter efeitos colaterais significativos.
- **POST**: criação ou ações com corpo; não idempotente por padrão.
- **PUT** / **PATCH**: substituição ou atualização parcial de recursos.
- **DELETE**: remoção; idempotência desejável no servidor.

## Códigos de status

- **2xx**: sucesso (**200** OK, **201** criado, **204** sem conteúdo).
- **3xx**: redirecionamento (**301** permanente, **302/307** temporário).
- **4xx**: erro do cliente (**400** bad request, **401** não autenticado, **403** proibido, **404** não encontrado, **429** rate limit).
- **5xx**: erro do servidor (**500** interno, **502** bad gateway, **503** indisponível).

## REST

- Recursos nomeados por **URLs**; representações em **JSON** ou XML.
- **HATEOAS** (opcional): links na resposta para descobrir ações seguintes.
- Versionamento via path (`/v1/...`), header ou query — escolher um padrão por API.

## Exemplos com curl

GET com query string:

```bash
curl -sS "https://api.example.com/v1/items?limit=10&status=active"
```

POST com JSON:

```bash
curl -sS -X POST "https://api.example.com/v1/items" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"demo\", \"quantity\": 1}"
```

## Boas práticas

- **Paginação** (`limit`/`cursor`) e **filtros** estáveis para listas grandes.
- **Idempotency-Key** em POST sensíveis a duplicação (pagamentos).
- Documentar com **OpenAPI** (Swagger) para consumo previsível.
