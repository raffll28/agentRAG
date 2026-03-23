---
tags: [rede, tcp-ip, dns, networking]
---

# Rede: TCP/IP e DNS

## Modelo em camadas

- **TCP/IP** é a família de protocolos da internet: enlace, internet, transporte, aplicação.
- **IP** (IPv4/IPv6) fornece endereçamento e roteamento; pacotes podem ser fragmentados e reordenados na origem.

## TCP vs UDP

- **TCP**: orientado à conexão, confiável, ordenado; retransmissões e controle de congestionamento. Usado por HTTP/HTTPS, SSH, SMTP.
- **UDP**: sem conexão, baixa latência, sem garantia de ordem; adequado a DNS, VoIP, jogos em tempo real e streaming onde perdas pontuais são aceitáveis.

## Portas e firewalls

- **Portas** (0–65535) multiplexam serviços em um mesmo IP; **well-known** (ex.: 80, 443) são convenções, não obrigações.
- **Firewalls** filtram por IP, porta, protocolo e estado da conexão (**stateful**).

## DNS

- **DNS** traduz nomes (ex.: `example.com`) em endereços IP.
- Registros comuns: **A** / **AAAA** (endereço), **CNAME** (alias), **MX** (e-mail), **TXT** (SPF, verificações).
- **TTL** controla cache; mudanças de DNS podem demorar a propagar.
- **DNS sobre HTTPS** (DoH) e **TLS** (DoT) aumentam privacidade em relação a consultas em texto claro.

Consulta rápida no terminal:

```bash
dig +short A example.com
nslookup example.com
```

## NAT e endereços privados

- **NAT** mapeia vários hosts internos para um IP público; **IPv6** reduz dependência de NAT em redes novas.

## Boas práticas

- Preferir **IPv6** onde disponível; testar conectividade com `ping`, `traceroute`, `curl`.
- Documentar **subnets** e **VPC** em ambientes de nuvem para evitar sobreposição com redes on-premise.
