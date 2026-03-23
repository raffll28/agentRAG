---
tags: [observabilidade, logs, metricas, traces]
---

# Observabilidade e logging

## Três pilares

- **Logs**: eventos discretos com contexto (nível, timestamp, request id).
- **Métricas**: séries temporais agregadas (latência p99, taxa de erro, uso de CPU).
- **Traces**: rastreamento distribuído de uma requisição através de serviços (**OpenTelemetry**).

## Logs estruturados

- **JSON** facilita ingestão em ELK, Loki, CloudWatch.
- Campos estáveis: `level`, `msg`, `service`, `trace_id`, `user_id` (hash).

## Correlação

- **Trace ID** propagado em headers (W3C Trace Context) liga logs e spans.
- **Span** representa operação; **trace** agrupa spans de uma carga útil.

## Alertas

- Alertar sobre **SLOs** (ex.: erro > 1% por 5 min), não só CPU alta sem contexto.
- **Runbooks** ligados a alertas reduzem tempo de resolução.

## Boas práticas

- Níveis **DEBUG** apenas em dev; **INFO** para fluxo normal; **ERROR** com stack quando aplicável.
- **Sampling** de traces em alto volume para custo controlado.
