---
tags: [unicode, utf-8, encoding]
---

# Codificação e Unicode

## Unicode

- **Code points** abrangem praticamente todos os sistemas de escrita; **UTF-8** é a codificação variável de largura dominante na web e em Unix.
- **UTF-16** e **UTF-32** aparecem em APIs legadas (Windows, Java internamente).

## UTF-8

- Compatível com ASCII nos primeiros 128 valores; multibyte para demais caracteres.
- **BOM** UTF-8 (`EF BB BF`) é opcional e às vezes indesejada em arquivos de código.

## Erros comuns

- Ler bytes como **latin1** quando são UTF-8 produz mojibake (caracteres errados).
- **Unicode normalization** (NFC vs NFD) afeta comparação de strings em buscas e filenames.

## Python

- **`str`** é Unicode; I/O usa **encoding** explícito (`encoding="utf-8"` em `open`).
- **`errors=`**: `strict` (padrão), `replace`, `ignore` — preferir corrigir a fonte.

```python
with open("data.txt", encoding="utf-8") as f:
    text = f.read()
```

## JSON e APIs

- JSON exige texto Unicode; em HTTP usar **charset=utf-8** no **Content-Type**.

## Boas práticas

- Padronizar **UTF-8** em repositórios, editores e servidores.
- Normalizar NFC antes de indexar texto para busca consistente.
