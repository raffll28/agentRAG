---
tags: [git, versionamento, workflow]
---

# Git e fluxos de trabalho

## Conceitos básicos

- **Repositório**: histórico de commits; **branch** é um ponteiro móvel.
- **merge** integra históricos; **rebase** reescreve commits em cima de outra base (uso com cuidado em branches públicos).
- **.gitignore** evita versionar artefatos de build e segredos.

## Fluxos comuns

- **Trunk-based**: poucos branches longos; integração frequente na `main`.
- **Git Flow**: `develop`, `release`, `hotfix` — mais cerimônia, comum em releases lentos.
- **GitHub Flow**: PRs contra `main` com deploy contínuo.

## Pull requests

- **Revisão** de código, CI verde, descrição clara do que e por quê.
- Commits pequenos e mensagens no padrão **Conventional Commits** facilitam changelog.

## Conflitos

- Editar manualmente marcadores `<<<<<<<`, `=======`, `>>>>>>>`, ou usar ferramentas de merge.
- Preferir **rebase interativo** para limpar histórico local antes do push.

Fluxo curto em branch de feature:

```bash
git checkout -b feat/login-validation
# ... commits ...
git fetch origin
git rebase origin/main
# antes de merge: squash ou editar mensagens (cuidado em branches compartilhados)
# git rebase -i HEAD~3
```

Mensagem no padrão **Conventional Commits**:

```text
feat(auth): validate email format on signup
```

## Segredos

- Nunca commitar **tokens**; usar **git-secrets**, **pre-commit** hooks e **secret scanning** no provedor.

## Boas práticas

- **Tags** para releases; **signed commits** opcional para auditoria.
- **Large files**: Git LFS para binários pesados.
