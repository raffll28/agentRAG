---
tags: [linux, shell, bash, posix]
---

# Linux e shell — básicos

## Filesystem

- Raiz **`/`**; diretórios importantes: **`/etc`** (config), **`/var/log`**, **`/home`**, **`/tmp`**.
- **Permissões** rwx para user/group/other; **chmod**, **chown** com cuidado (root).

## Shell

- **bash** e **sh** são comuns; scripts começam com **shebang** `#!/usr/bin/env bash`.
- **pipes** (`|`) conectam stdout de um comando ao stdin do próximo.
- **Redirecionamentos**: `>` sobrescreve, `>>` anexa, `2>` para stderr.

Contar linhas que contêm uma palavra em arquivos `.log`:

```bash
grep -h "ERROR" /var/log/myapp/*.log | wc -l
```

Permissões numéricas comuns: `644` (rw-r--r--) para arquivo, `755` (rwxr-xr-x) para script executável:

```bash
chmod 644 config.yml
chmod 755 deploy.sh
```

## Processos

- **`ps`**, **`top`** / **`htop`**, **`kill`** / **`kill -9`** (último recurso).
- **`nohup`** e **`&`** para background; **systemd** gerencia serviços modernos (**`systemctl`**).

## Rede (CLI)

- **`ip`**, **`ss`**, **`curl`**, **`dig`**, **`ping`** para diagnóstico.
- **SSH** para acesso remoto; chaves **ed25519** preferíveis a RSA legado.

## Pacotes

- **apt** (Debian/Ubuntu), **dnf/yum** (Fedora/RHEL), **pacman** (Arch).
- Evitar `curl | bash` de fontes não confiáveis.

## Boas práticas

- Mínimo privilégio; **sudo** com timestamp; auditar `/etc/sudoers`.
- **Cron** / **timers systemd** para tarefas agendadas; logs em **journalctl**.
