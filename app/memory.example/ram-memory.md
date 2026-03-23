---
tags: [hardware, ram, memoria, ddr]
---

# Memória RAM

## Função

A **RAM** (memória volátil) guarda dados e programas em uso com latência muito menor que SSD ou disco. Mais RAM permite mais aplicações abertas, VMs maiores e buffers (navegador, IDEs, bancos em memória).

## DDR4 e DDR5

- **DDR4**: padrão maduro; frequências comuns em MHz efetivos (ex.: 3200).
- **DDR5**: maior largura de banda por pino, bancos e densidades maiores; frequências base mais altas; **PMIC** no módulo em muitos designs.

## Canais e encaixe

- **Dual channel** (dois módulos em slots pareados): dobra largura de banda teórica versus single channel — recomendado em desktops e laptops com dois slots.
- **SODIMM**: formato compacto em notebooks; **DIMM** em desktops; **CAMM** / soldada em alguns ultrafinos.

## Capacidade típica

- **8 GB**: mínimo funcional para desktop leve.
- **16 GB**: confortável para uso geral e desenvolvimento.
- **32 GB+**: edição de vídeo, VMs, datasets locais, servidores de desenvolvimento.

## ECC (Error-Correcting Code)

- Detecta/corrige erros de bit; comum em **servidores** e workstations (requer CPU/chipset/módulos **ECC** compatíveis).
- **Non-ECC**: padrão em PCs domésticos.

## Latência e XMP / EXPO

- Timings (**CL**, tRCD, etc.) e frequência definem latência efetiva.
- Perfis **XMP** (Intel) e **EXPO** (AMD) no BIOS aplicam velocidades acima do JEDEC padrão — verificar compatibilidade na placa-mãe.
- Ativar perfis overclock de RAM pode exigir **atualização de BIOS** estável e lista de QVL do fabricante da placa.

## Estabilidade e integridade

- **Rowhammer**-class mitigations existem em firmware e controladores; em servidores, **ECC** reduz risco de bit flips silenciosos em cargas 24/7.

## Integrada vs dedicada (GPU)

- GPUs integradas usam parte da **RAM do sistema** como VRAM; quanto mais RAM e dual channel, melhor o desempenho gráfico integrado.
