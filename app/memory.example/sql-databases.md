---
tags: [sql, banco-de-dados, postgres, mysql]
---

# Bancos relacionais (SQL)

## Conceitos

- **Tabelas** com **linhas** e **colunas**; **chave primária** identifica unicamente cada linha.
- **Chaves estrangeiras** modelam relacionamentos e podem ter políticas **ON DELETE/UPDATE**.
- **ACID**: atomicidade, consistência, isolamento, durabilidade — base de transações confiáveis.

## SQL essencial

- **SELECT** com **JOIN** (INNER, LEFT, RIGHT), **WHERE**, **GROUP BY**, **HAVING**, **ORDER BY**.
- **Índices** (B-tree comum) aceleram buscas e ordenação; custo extra em escritas.
- **EXPLAIN** / **EXPLAIN ANALYZE** revelam planos de execução e custos.

Exemplo de join:

```sql
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON o.user_id = u.id
WHERE o.created_at >= '2026-01-01'
ORDER BY o.total DESC;
```

Inspecionar plano (PostgreSQL):

```sql
EXPLAIN ANALYZE
SELECT id FROM orders WHERE user_id = 42;
```

## Produtos populares

- **PostgreSQL**: recursos avançados (JSON, arrays, extensões), forte em consistência.
- **MySQL/MariaDB**: amplamente hospedado em LAMP; **InnoDB** para transações.
- **SQLite**: arquivo único, zero servidor; ideal para apps embutidas e testes.

## Migrações

- **Migrações versionadas** (Flyway, Alembic, Prisma migrate) evitam drift entre ambientes.
- Backup antes de mudanças destrutivas; testar em staging.

## Boas práticas

- Evitar **N+1 queries**; usar joins ou batch loading.
- **Connection pooling** (PgBouncer, pool no app) para reduzir overhead de conexões.
