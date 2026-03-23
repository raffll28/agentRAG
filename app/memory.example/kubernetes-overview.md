---
tags: [kubernetes, k8s, orquestracao]
---

# Kubernetes — visão geral

## Objetos principais

- **Pod**: menor unidade agendável; compartilha rede e volumes entre containers do mesmo pod.
- **Deployment**: replica sets e atualizações rolantes (**rolling update**).
- **Service**: IP virtual estável e **load balancing** para pods por **labels**.
- **Ingress**: roteamento HTTP(S) externo para services.

## Configuração

- **ConfigMap** para config não sensível; **Secret** para dados sensíveis (base64 no etcd — criptografia em repouso recomendada).
- **Namespaces** isolam equipes/ambientes na mesma cluster.

## Recursos e escalabilidade

- **Requests** e **limits** de CPU/memória evitam starvation e OOM kills.
- **HPA** (Horizontal Pod Autoscaler) escala réplicas por métricas (CPU, custom metrics).

## Armazenamento

- **PersistentVolume** / **PersistentVolumeClaim** abstraem discos; **StorageClass** provisiona dinamicamente.

## Operação

- **kubectl** para inspeção e apply de manifests (YAML).
- **Helm** empacota charts com templates; **Kustomize** sobrepõe patches por ambiente.

Comandos frequentes (substitua `my-namespace`):

```bash
kubectl get pods -n my-namespace
kubectl describe pod my-pod -n my-namespace
kubectl apply -f manifest.yaml
```

## Boas práticas

- **Liveness** vs **readiness** probes distintas; readiness remove tráfego sem reiniciar o pod.
- Imagem imutável por digest; políticas de **imagePull** e **securityContext**.
