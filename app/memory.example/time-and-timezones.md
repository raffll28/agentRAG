---
tags: [tempo, timezone, utc, iso8601]
---

# Tempo e fusos horários

## UTC

- **UTC** é referência civil universal; armazenar instantes em UTC evita ambiguidade.
- **Unix timestamp** (segundos desde epoch) é timezone-agnostic.

## Timezones

- **IANA** names (`America/Sao_Paulo`) lidam com **DST** (horário de verão) historicamente.
- **Offsets** fixos (`UTC-3`) ignoram mudanças sazonais — evitar para dados de longo prazo.

## ISO 8601

- Formato **`2026-03-23T14:30:00Z`** (Z = UTC) ou com offset **`2026-03-23T11:30:00-03:00`**.
- **Date-only** (`2026-03-23`) sem hora para aniversários e vencimentos “calendário”.

Exemplos lado a lado:

```text
2026-03-23T17:00:00Z          # UTC
2026-03-23T14:00:00-03:00     # mesmo instante, offset São Paulo (sem DST)
```

## APIs e bancos

- **PostgreSQL**: `timestamptz` armazena UTC internamente; cliente converte para sessão.
- **JavaScript**: `Date` é milissegundos UTC; formatação local depende do runtime.

## Boas práticas

- Nunca interpretar string datetime sem timezone em sistemas distribuídos.
- Testes com **freezegun** ou clock injetável para determinismo.
