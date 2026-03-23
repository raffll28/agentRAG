---
tags: [hardware, armazenamento, ssd, hdd, nvme]
---

# Armazenamento (drives)

## HDD (disco magnético)

- **Platos e cabeçote**: leitura mecânica; bom **custo por TB** para arquivo e backup.
- **RPM** (5400/7200): impacta latência sequencial e seek.
- **Fragilidade a impactos** em uso (especialmente laptops).

## SSD SATA

- Interface **SATA III** (~600 MB/s teóricos); substitui HDD em formato 2,5" ou M.2 SATA.
- Ganho enorme de **IOPS** e latência versus HDD.

## SSD NVMe (PCIe)

- Conecta via **PCIe** (M.2 ou U.2); largura de banda muito superior (PCIe 3.0/4.0/5.0).
- **DRAM cache** no SSD pode ajudar consistência sob carga mista; modelos DRAM-less usam mapeamento host/HMB.
- **TBW** (terabytes gravados): desgaste estimado da NAND; relevante para cargas de escrita intensiva.
- **TLC / QLC**: células multi-bit; QLC costuma ser mais barato por GB com endurance menor — adequado a leitura predominante.

## Encriptação em repouso

- **BitLocker** (Windows), **FileVault** (macOS), **LUKS** (Linux) protegem dados se o disco for removido ou roubado; combine com **TPM** ou senha forte de recuperação.

## Form factors

- **M.2 2280**: mais comum em desktops e notebooks modernos.
- **2,5"**: SATA SSD e HDD.
- **NVMe add-in card**: placas PCIe em workstations/servidores.

## RAID e volumes

- **RAID 0**: striping, velocidade, sem redundância.
- **RAID 1**: espelho, redundância.
- **RAID 5/6/10**: comuns em servidores com controladoras ou software RAID.

## Sistemas de arquivos e SO

- **NTFS / exFAT** no Windows; **APFS** no macOS; **ext4 / Btrfs / xfs** no Linux.
- **TRIM** ajuda desempenho de SSD ao informar blocos livres ao controlador.

## Boas práticas

- SSD **NVMe** para SO, apps e projetos ativos; HDD ou SSD barato para **backup** e mídia fria.
- Monitorar saúde via **SMART** (CrystalDiskInfo, `smartctl`, etc.).
