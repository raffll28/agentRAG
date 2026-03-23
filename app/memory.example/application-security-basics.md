---
tags: [seguranca, owasp, appsec]
---

# Segurança de aplicações — básicos

## Superfícies de ataque

- **Entrada do usuário** nunca é confiável: validação, sanitização e encoding corretos por contexto (HTML, SQL, shell).
- **Autenticação** (quem é) separada de **autorização** (o que pode fazer).

## OWASP Top 10 (resumo)

- **Injection** (SQL, command, LDAP): usar queries parametrizadas e APIs seguras.
- **Broken access control**: checar permissões em cada operação sensível.
- **Cryptographic failures**: TLS em trânsito; algoritmos e chaves atuais em repouso.
- **XSS**: escapar saída; **CSP** restringe scripts.
- **CSRF**: tokens ou cookies **SameSite** em sessões baseadas em cookie.

## Segredos

- **Variáveis de ambiente** ou cofres (**Vault**, cloud secret managers); não hardcodar em código.
- Rotação periódica de chaves API e senhas.

## Dependências

- **CVEs** em bibliotecas: automação de alerta e upgrades planejados.
- Revisar permissões de pacotes em registries (typosquatting).

## Logging e privacidade

- Não logar **PII** ou tokens; mascarar identificadores quando necessário.
- **LGPD/GDPR**: base legal, minimização e retenção definidas.

## Boas práticas

- **Threat modeling** em features novas; **pentest** periódico em sistemas expostos.
