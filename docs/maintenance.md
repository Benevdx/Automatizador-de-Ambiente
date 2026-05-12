# Manutenção

## Atualizar o sistema

Opção 3 no menu, ou manualmente:

- Linux: `sudo apt update && sudo apt upgrade -y`
- Windows: `winget upgrade --all`

## Adicionar nova tecnologia

Edite `configs/technologies.json`:

```json
"NomeTech": {
  "linux": "comando linux",
  "windows": "winget install pacote"
}
```

## Adicionar pacotes ao ambiente Python padrão

Edite `configs/python_envs.json` → lista `default_packages`.

## Logs

Armazenados em `logs/install_YYYYMMDD.log`.

## Backup de dotfiles

Opção 4 no menu. Copia `.bashrc`, `.gitconfig`, `.zshrc`, `.ssh/config` para `backup_YYYYMMDD_HHMMSS/`.
