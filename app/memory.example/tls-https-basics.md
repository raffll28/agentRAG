---
tags: [tls, https, seguranca, criptografia]
---

# TLS e HTTPS

## O que o TLS faz

- **TLS** (sucessor de SSL) fornece **confidencialidade** (criptografia), **integridade** (MAC/autenticação) e **autenticação do servidor** (certificado).
- **HTTPS** é HTTP sobre TLS (porta **443** por convenção).

## Certificados

- **Cadeia de confiança**: certificado do servidor é assinado por uma **CA** (autoridade certificadora); raízes confiáveis ficam no SO ou no browser.
- **Let's Encrypt** emite certificados gratuitos de curta duração com renovação automatizada (**ACME**).
- **SAN** e **wildcard** (`*.example.com`) cobrem múltiplos hostnames.

## Handshake

- Cliente e servidor negociam versão TLS, conjuntos de cifras e trocam chaves (**ECDHE** comum).
- **HSTS** força HTTPS por um período; reduz downgrade para HTTP claro.

## Erros comuns

- Certificado expirado ou nome (**CN/SAN**) não batendo com o host.
- Mistura **HTTP** e **HTTPS** (conteúdo misto) bloqueada por browsers.
- Protocolos obsoletos (**SSLv3**, **TLS 1.0/1.1**) devem ser desabilitados no servidor.

## Boas práticas

- **TLS 1.2+** mínimo; preferir **TLS 1.3** onde suportado.
- Redirecionar **HTTP → HTTPS** com **301** e cabeçalhos de segurança (**CSP**, **X-Frame-Options**, etc.) conforme política.

Inspeção manual do handshake (substitua host; interrompa com Ctrl+C após ver o certificado):

```bash
openssl s_client -connect example.com:443 -servername example.com
```
