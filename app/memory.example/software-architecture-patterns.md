---
tags: [arquitetura, software, monolito, microservicos, ddd]
---

# Arquiteturas de software — padrões

## Monólito vs microsserviços vs monólito modular

- **Monólito**: um deploy único; transações e refatoração simples entre módulos; escala vertical ou réplicas idênticas.
- **Microsserviços**: serviços independentes, deploy e escala por fronteira; exige rede, observabilidade, consistência eventual e **DevOps** maduro.
- **Monólito modular**: um repositório/deploy com **módulos** claros (fronteiras de domínio) — prepara evolução sem o custo operacional inicial de microserviços.

## Camadas

- **Apresentação** (UI/API) → **aplicação** (orquestração) → **domínio** (regras) → **infraestrutura** (DB, filas, HTTP externos).
- **Regra**: dependências apontam para dentro (domínio sem conhecer detalhes de framework).

## Hexagonal (ports and adapters)

- **Núcleo** de domínio expõe **ports** (interfaces); **adapters** implementam DB, fila, UI.
- Facilita testes com **doubles** e troca de tecnologia sem reescrever regras.

## Event-driven e mensageria

- Serviços publicam **eventos**; consumidores reagem de forma assíncrona; desacopla picos e equipes.
- Detalhes de filas e streams: ver `message-queues-and-streams.md`.

## CQRS

- **Command Query Responsibility Segregation**: modelos de escrita e leitura separados; leituras otimizadas (views, caches) sem sobrecarregar o modelo transacional.
- Útil quando padrões de acesso leitura/escrita são muito diferentes.

## Twelve-Factor App

- Config por **ambiente**, logs como **stream**, **stateless** processes, **dependency** explícita — alinhado a boas práticas de deploy em containers; ver também `software.md` (CI/CD e dependências).

## Quando usar o quê

- **Time pequeno / produto inicial**: monólito ou monólito modular com testes e módulos claros.
- **Domínios independentes e escala heterogênea**: considerar microsserviços após dor real (não por moda).
- **Eventos** quando integrações assíncronas e tolerância a latência forem aceitáveis.
- **CQRS** quando relatórios e consultas pesadas competem com escrita transacional.

## Boas práticas

- Fronteiras alinhadas ao **negócio**, não só à tecnologia.
- Documentar contratos de API e eventos; versionar com compatibilidade.
- Observabilidade (logs, métricas, traces) desde o início em sistemas distribuídos.
