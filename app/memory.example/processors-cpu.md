---
tags: [hardware, cpu, processador, nucleos]
---

# Processadores (CPU)

## Papel no sistema

A **CPU** executa o sistema operacional, aplicações gerais e orquestra GPU, disco e rede. Latência e desempenho single-thread ainda importam para muitas cargas.

## Núcleos e threads

- **Núcleos físicos**: unidades de execução reais.
- **Threads lógicas** (SMT / Hyper-Threading): dois fluxos por núcleo em muitas arquiteturas, melhorando paralelismo leve.
- Cargas **multithread** (compilação, render CPU, servidores) se beneficiam de mais núcleos.

## Fabricantes e linhas

- **Intel**: Core (i3/i5/i7/i9), Xeon (servidor/workstation); arquiteturas híbridas **P-core / E-core** em modelos recentes (desempenho vs eficiência).
- **AMD**: Ryzen (desktop/mobile), Threadripper (HEDT/workstation), EPYC (servidor).
- **Apple Silicon**: M1/M2/M3… (ARM) com CPU+GPU+Neural Engine integrados.

## Nomes comerciais vs identificação técnica

- Marcas como **Core i7** ou **Ryzen 7** indicam posicionamento de mercado; o **SKU** completo (ex.: números-sufixo de geração, letras **H/K/U**) define TDP, gráficos integrados e recursos exatos.
- Comparar sempre **geração** e **arquitetura** (nome em código), não só o dígito da série.

## Clock e TDP

- **Frequência base / boost**: picos curtos elevam desempenho sob refrigeração e energia adequadas.
- **TDP / PBP**: guia de consumo térmico; laptops priorizam variantes de baixa voltagem (**U**, **P**, **H** em nomenclaturas móveis).

## Cache

- **L1 / L2 / L3**: hierarquia reduz latência versus RAM; **L3** maior costuma ajudar jogos e workloads mistos.

## Instruções e segurança

- Extensões **AVX-512 / AVX2** aceleram vetores em software compatível.
- Mitigações de **Spectre/Meltdown** e similares podem ter custo de desempenho em alguns cenários.

## Escolha resumida

- **Jogos**: forte desempenho single-thread + GPU adequada; 6+ núcleos modernos costuma bastar.
- **Servidor / VMs**: muitos núcleos, ECC com chipset/plataforma compatível, TDP sustentável.
