import os
import json
import platform
import subprocess
import logging
from datetime import datetime

os.makedirs("logs", exist_ok=True)
LOG_FILE = f"logs/install_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)
log = logging.getLogger()

CONFIG_PATH = "configs/technologies.json"
PYTHON_ENV_PATH = "configs/python_envs.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def detect_os():
    s = platform.system()
    if s == "Windows":
        return "windows"
    elif s == "Linux":
        return "linux"
    else:
        raise SystemExit("Sistema operacional não suportado.")


def run(cmd):
    log.info(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        log.warning(f"Comando retornou código {result.returncode}")


def menu(title, options):
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    for i, opt in enumerate(options, 1):
        print(f"  [{i}] {opt}")
    print(f"{'='*40}")
    while True:
        try:
            choice = int(input("Escolha: "))
            if 1 <= choice <= len(options):
                return choice
        except (ValueError, KeyboardInterrupt):
            pass
        print("Opção inválida.")


def checkbox(title, options):
    print(f"\n{title}")
    print("(números separados por vírgula | 'a' para todos)\n")
    for i, opt in enumerate(options, 1):
        print(f"  [{i:>2}] {opt}")
    raw = input("\nSeleção: ").strip()
    if raw.lower() == "a":
        return options
    try:
        indices = [int(x.strip()) - 1 for x in raw.split(",")]
        return [options[i] for i in indices if 0 <= i < len(options)]
    except ValueError:
        print("Entrada inválida.")
        return []


def install_technologies():
    os_type = detect_os()
    techs = load_json(CONFIG_PATH)
    selected = checkbox("Selecione as tecnologias:", list(techs.keys()))
    if not selected:
        print("Nenhuma tecnologia selecionada.")
        return
    for tech in selected:
        log.info(f"Instalando {tech}...")
        run(techs[tech][os_type])
    print(f"\n✓ {len(selected)} tecnologia(s) instalada(s).")


def create_python_env():
    env_name = input("\nNome do ambiente virtual: ").strip()
    if not env_name:
        print("Nome inválido.")
        return
    py = "python3" if platform.system() == "Linux" else "python"
    if subprocess.run(f"{py} -m venv {env_name}", shell=True).returncode != 0:
        log.error("Falha ao criar ambiente virtual.")
        return
    config = load_json(PYTHON_ENV_PATH)
    pip = (
        f"{env_name}/bin/pip"
        if platform.system() == "Linux"
        else f"{env_name}\\Scripts\\pip.exe"
    )
    for pkg in config["default_packages"]:
        run(f"{pip} install {pkg}")
    print(f"\n✓ Ambiente '{env_name}' criado.")


def update_system():
    os_type = detect_os()
    print("\nAtualizando sistema...")
    run(
        "sudo apt update && sudo apt upgrade -y"
        if os_type == "linux"
        else "winget upgrade --all"
    )
    print("✓ Concluído.")


def backup_dotfiles():
    backup_dir = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(backup_dir, exist_ok=True)
    files = ["~/.bashrc", "~/.gitconfig", "~/.zshrc", "~/.ssh/config"]
    copied = 0
    for f in files:
        path = os.path.expanduser(f)
        if os.path.exists(path):
            run(f"cp {path} {backup_dir}/")
            copied += 1
    print(f"\n✓ Backup em '{backup_dir}' ({copied} arquivo(s)).")


def main():
    options = [
        "Instalar tecnologias",
        "Criar ambiente Python",
        "Atualizar sistema",
        "Backup de dotfiles",
        "Sair",
    ]
    actions = [install_technologies, create_python_env, update_system, backup_dotfiles]
    while True:
        choice = menu("DEV SETUP MANAGER", options)
        if choice <= len(actions):
            actions[choice - 1]()
        else:
            print("\nAté mais.\n")
            break


if __name__ == "__main__":
    main()