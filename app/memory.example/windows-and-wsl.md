---
tags: [windows, wsl, powershell]
---

# Windows e WSL

## Camadas do Windows

- **NT kernel**; subsistemas para Win32, **WSL2** (VM Linux leve via Hyper-V).
- **PowerShell** moderno: cmdlet, pipeline orientado a objetos; **cmd** legado ainda existe.

## WSL

- **WSL2** roda kernel Linux real; integração de rede e filesystem com Windows (**`/mnt/c`**).
- Distros via **Microsoft Store** ou importação manual; **`.wslconfig`** ajusta CPU/mem.
- Ferramentas Linux (**git**, **docker** via Docker Desktop com backend WSL) comuns em dev.

## Permissões

- **ACLs** NTFS mais ricas que Unix; **UAC** eleva privilégios sob demanda.
- **OneDrive** e caminhos longos: atenção a **MAX_PATH** e prefixo `\\?\`.

## Desenvolvimento

- **Visual Studio** / **VS Code** com extensões remotas para WSL.
- **winget** instala pacotes; **Chocolatey** alternativa comunitária.

## Boas práticas

- Preferir **LF** em projetos cross-platform (`.gitattributes`) para evitar diffs de linha.
- Antivírus pode bloquear scans em diretórios de build — exceções controladas.
