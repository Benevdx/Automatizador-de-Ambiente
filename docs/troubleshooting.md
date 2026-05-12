# Solução de Problemas

## Winget não encontrado

Atualize o App Installer pela Microsoft Store.

## Permissão negada (Linux)

Use `sudo` ou execute como root.

## Python não encontrado no PATH

- Linux: `which python3`
- Windows: reinstale marcando "Add to PATH".

## Docker: permissão negada após instalação

```bash
sudo usermod -aG docker $USER
newgrp docker
```

## VirtualBox + Hyper-V (Windows)

Desabilite o Hyper-V:

```powershell
bcdedit /set hypervisorlaunchtype off
```

Reinicie a máquina.

## mpi4py falha na instalação

Instale o MPICH antes: `sudo apt install -y mpich libmpich-dev`
