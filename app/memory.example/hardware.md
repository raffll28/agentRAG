---
tags: [hardware, infraestrutura]
---

# Hardware — referência para o agente

## CPU (processador)

- **Núcleos e threads**: núcleos físicos executam instruções; *threads* lógicas (hyper-threading/SMT) permitem mais fluxos concorrentes por núcleo.
- **Arquiteturas comuns**: x86-64 (PCs e servidores), ARM (mobile, Apple Silicon, servidores eficientes), RISC-V (em crescimento em embarcados e pesquisa).
- **Cache**: L1/L2/L3 reduzem latência versus RAM; workloads sensíveis a latência se beneficiam de cache maior.

## GPU

- Paralelismo massivo para gráficos, **machine learning** (CUDA, ROCm) e computação GPGPU.
- **VRAM**: memória dedicada na placa; modelos grandes de LLM local costumam exigir muita VRAM.

## Memória RAM

- **DDR4/DDR5**: padrões atuais em desktops/laptops; maior largura de banda e frequência melhoram throughput.
- **ECC**: memória com correção de erros, comum em servidores.

## Armazenamento

- **SSD NVMe**: interface PCIe; menor latência que SATA SSD ou HDD.
- **HDD**: melhor custo por TB, pior desempenho; ainda usado para arquivo frio.

## Rede

- **Ethernet**: 1 Gb/s comum; 10/25/100 Gb/s em datacenters.
- **Wi-Fi 6/6E/7**: maior capacidade e menor congestão em ambientes densos.

## Energia e resfriamento

- Datacenters medem **PUE** (eficiência energética). Throttling reduz clock quando há superaquecimento.

## Firmware e segurança de plataforma

- **BIOS / UEFI**: firmware que inicializa hardware e carrega o bootloader; UEFI substitui BIOS legado com partições GPT, boot mais rápido e recursos modernos.
- **Secure Boot**: só executa bootloaders assinados; reduz malware de pré-inicialização quando bem configurado.
- **TPM** (Trusted Platform Module): chip ou firmware para chaves criptográficas; usado por **BitLocker**, **Windows Hello**, medição de integridade e alguns requisitos corporativos.

## Periféricos e barramentos

- **USB**: USB-A/C; gerações **USB 3.x** (5–20 Gb/s) e **USB4** (inclui tunelamento Thunderbolt em muitos hosts); alimentação e dados no mesmo conector em Type-C.
- **Thunderbolt**: PCIe + DisplayPort tunelados; docks e eGPUs em estações de trabalho.

## Vídeo e áudio

- **Monitores**: resolução (1080p, 1440p, 4K), **taxa de atualização** (Hz), **HDR**, painéis IPS/OLED; **sync adaptativo** (G-Sync / FreeSync) reduz tearing.
- **Áudio**: codecs onboard, **DAC/AMP** externos para fones; **Bluetooth** para áudio sem fio com codecs (AAC, aptX, LDAC) variando em latência e qualidade.

## Aprofundar nesta pasta

- CPU detalhada: `processors-cpu.md`.
- RAM: `ram-memory.md`.
- GPU: `video-cards-gpu.md`.
- Armazenamento: `storage-drives.md`.
- Este arquivo é visão geral; números de modelo e especificações aprofundadas ficam nos arquivos especializados acima.
