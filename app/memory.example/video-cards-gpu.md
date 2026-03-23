---
tags: [hardware, gpu, placa-de-video, vram]
---

# Placas de vídeo (GPU)

## Função

A **GPU** (Graphics Processing Unit) renderiza imagens e acelera cargas paralelizáveis: jogos, edição de vídeo, **machine learning** e computação GPGPU.

## Fabricantes principais

- **NVIDIA**: arquiteturas recentes (ex.: famílias GeForce RTX, workstation Quadro/RTX Ada); ecossistema **CUDA** dominante em ML e render.
- **AMD**: linhas Radeon RX; suporte **ROCm** em Linux para compute; **FSR** (upscaling) em jogos.
- **Intel**: Arc (consumo) e integradas Xe; evolução rápida no mercado de entrada/intermediário.

## VRAM (memória de vídeo)

- Armazena texturas, buffers de frame e pesos de modelos em inferência local de **LLM**.
- **Capacidade insuficiente** força offload para RAM (mais lento) ou impede carregar o modelo.
- **Largura de barramento** e geração de memória (GDDR6, GDDR6X, HBM em datacenter) afetam largura de banda.

## Barramento e alimentação

- **PCIe**: x16 é comum em desktops; laptops usam variantes móveis ou GPUs soldadas.
- **Consumo (TDP)**: placas exigem fonte adequada; conectores **6/8 pin PCIe** ou **12VHPWR** (12+4) em modelos recentes.

## Ray tracing e upscaling

- **RT cores**: aceleram raios para iluminação realista.
- **DLSS** (NVIDIA), **FSR** (AMD), **XeSS** (Intel): reconstrução/upscaling com IA para mais FPS.
- **Frame generation** (ex.: DLSS 3 com **Frame Generation**): interpola quadros para FPS maior; pode adicionar latência em jogos competitivos.

## Sincronização com o monitor

- **VRR** (Variable Refresh Rate): **G-Sync Compatible** / **FreeSync** alinham taxa de atualização do painel ao framerate da GPU, reduzindo stutter e tearing sem VSYNC rígido.

## Uso em IA local

- Frameworks como **Ollama** podem usar GPU para inferência; requisitos dependem do **tamanho do modelo** e quantização.
