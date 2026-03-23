---
tags: [filesystem, paths, permissoes]
---

# Caminhos e permissões de arquivo

## Caminhos

- **Absolutos** desde raiz (`/home/user` em Unix, `C:\Users\...` no Windows).
- **Relativos** dependem do diretório de trabalho atual (**cwd**).
- **`.`** e **`..`** para atual e pai; normalizar com **`pathlib`** (Python) ou APIs nativas.

Preferir APIs em vez de juntar strings (evita bugs de separador):

```python
from pathlib import Path

base = Path("/var/app")
config = base / "config" / "settings.yml"  # correto em Unix e Windows
```

Anti-padrão frágil: `"C:\\Users\\me\\" + "file.txt"` ou misturar `/` e `\` manualmente.

## Separadores

- **Unix**: `/` ; **Windows**: `\` ou `/` em muitas APIs modernas.
- **UNC** `\\server\share` em redes Windows.

## Permissões Unix

- Bits **rwx** para dono, grupo e outros; diretórios precisam de **x** para travessia.
- **umask** mascara permissões na criação de arquivos.

## Links

- **Hard links** mesmo inode; **symlinks** podem apontar entre filesystems e quebrar se alvo mover.

## Boas práticas

- Evitar concatenar strings manualmente; usar bibliotecas de path.
- Validar que paths resolvidos ficam **abaixo** do diretório permitido (**jail** / **chroot** lógico) — padrão usado na leitura segura de memória do agente.
