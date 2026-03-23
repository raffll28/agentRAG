---
tags: [filas, kafka, rabbitmq, mensageria]
---

# Filas e streams

## Filas de mensagens

- **Producers** enviam mensagens para **brokers**; **consumers** processam de forma assíncrona.
- Desacopla picos de carga e permite **retries** com **dead-letter queues**.

## Padrões

- **At-least-once**: pode haver duplicatas; consumidores devem ser **idempotentes** ou usar deduplicação.
- **Exactly-once** é difícil de garantir de ponta a ponta; frequentemente combina **offsets** + idempotência.
- **Particionamento** em Kafka distribui carga e mantém ordem **por partição**.

## RabbitMQ

- **Exchanges** (direct, topic, fanout) roteiam para **queues**; AMQP 0-9-1.
- Bom para workloads de fila clássica e roteamento flexível.

## Apache Kafka

- **Log distribuído** com retenção configurável; **consumer groups** escalam leitura.
- **Schema Registry** (Avro/JSON/Protobuf) com versionamento de esquemas.
- Operação mais pesada que RabbitMQ; brilha em alto volume e replay.

## Boas práticas

- **Timeouts** e **limites de reprocessamento**; monitorar **lag** de consumidores.
- Mensagens pequenas; payloads grandes vão para **object storage** com referência na fila.
