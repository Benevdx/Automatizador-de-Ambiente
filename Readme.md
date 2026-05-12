# Dev Setup Manager

Gerenciador pessoal de ambiente de desenvolvimento — multiplataforma (Linux/Windows).

## Requisitos

- Python 3.10+
- Linux: `sudo`, `apt`, `curl` | Windows: Winget, PowerShell 5+

## Instalação

```bash
git clone <repo-url>
cd DevSetupManager
pip install -r requirements.txt
python install.py
```

## Menu

[1] Instalar tecnologias — seleção interativa via terminal \
[2] Criar ambiente Python — venv com pacotes padrão \
[3] Atualizar sistema — apt upgrade / winget upgrade \
[4] Backup de dotfiles — copia configs para pasta local \
[5] Sair

## Estrutura

DevSetupManager/  \
├── install.py    
├── requirements.txt
├── README.md
├── configs/
│ ├── technologies.json
│ ├── python_envs.json
│ └── vscode_extensions.txt
├── docs/
│ ├── maintenance.md
│ └── troubleshooting.md
├── dotfiles/ ← vazio, para seus arquivos
└── logs/ ← gerado automaticamente

## Adicionar tecnologia

Edite `configs/technologies.json` com o comando para cada plataforma.

## Logs

Gerados automaticamente em `logs/install_YYYYMMDD.log`.
