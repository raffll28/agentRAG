---
tags: [software, sistemas]
---

# Software — referência para o agente

## Sistemas operacionais

- **Linux**: kernel open source; distribuições (Ubuntu, Debian, Fedora) para servidor e desktop.
- **Windows**: desktop e servidor; integração com AD/Azure em empresas.
- **macOS**: ecossistema Apple; base Unix.

## Open source vs proprietário

- **Open source**: código disponível sob licença (MIT, Apache-2.0, GPL); comunidade e auditoria.
- **Proprietário**: licença comercial; suporte e roadmap controlados pelo fornecedor.

## Desenvolvimento

- **Controle de versão**: Git é o padrão; plataformas como GitHub/GitLab hospedam repositórios.
- **CI/CD**: pipelines automatizam testes e deploy (GitHub Actions, GitLab CI, Jenkins).
- **Containers**: Docker empacota apps; Kubernetes orquestra em escala.
- Fluxos Git e exemplos de comandos: `git-workflows.md`; testes e pytest: `testing-and-ci.md`.

## Gerenciamento de pacotes e versões

- **npm / yarn / pnpm** (JavaScript), **Cargo** (Rust), **pip** e **uv** (Python): instalam dependências e resolvem árvores de pacotes.
- **Semver** (major.minor.patch): mudanças incompatíveis elevam **major**; correções de bug elevam **patch**.
- **Ambientes virtuais** (venv, `uv` workspace): isolam dependências por projeto e evitam conflito global.

## Cadeia de suprimentos e segurança de build

- **Lockfiles** fixam versões exatas para builds reproduzíveis.
- **SBOM** (Software Bill of Materials): inventário de componentes para auditoria e resposta a CVEs.
- Ferramentas de **SAST/DAST** e varredura de dependências complementam revisão humana.

## Licenças

- **MIT/Apache-2.0**: permissivas; uso comercial comum.
- **GPL**: copyleft; derivados podem precisar manter a mesma liberdade.

## Segurança

- **Dependências**: lockfiles (`uv.lock`, `package-lock.json`) fixam versões.
- **Atualizações**: patches de segurança devem ser aplicados com prioridade.

## APIs e integração

- **REST**: HTTP + JSON; amplamente usado.
- **gRPC**: RPC binário, bom para serviços internos de baixa latência.
