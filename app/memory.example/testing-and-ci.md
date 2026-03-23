---
tags: [testes, pytest, ci, qualidade]
---

# Testes e CI

## Pirâmide de testes

- **Unitários**: rápidos, isolados, mocks controlados.
- **Integração**: DB, filas, APIs reais em ambiente de teste.
- **E2E**: fluxos completos; mais lentos e frágeis a timing.

## Boas práticas

- **AAA** (Arrange, Act, Assert) ou equivalente para clareza.
- **Dados de teste** determinísticos; evitar dependência de rede externa em CI.
- **Cobertura** é métrica auxiliar; não substitui testes de comportamento.

## Python / pytest

- **Fixtures** para setup/teardown; **parametrize** para casos múltiplos.
- **Markers** para categorizar testes lentos ou integração.
- **monkeypatch** para substituir dependências sem alterar código de produção.

Teste unitário mínimo:

```python
def test_sum_positive():
    assert 1 + 2 == 3
```

## CI

- Pipeline em cada push/PR: **lint**, **testes**, opcionalmente **build** de imagem.
- Falhar rápido; cache de dependências (`uv`, `pip`, `npm`) reduz tempo.
- **Artifacts** e **logs** retidos para depuração.

## Qualidade contínua

- **Type checkers** (mypy, pyright) em modo strict progressivo.
- **SAST** e **dependabot** para vulnerabilidades conhecidas.
