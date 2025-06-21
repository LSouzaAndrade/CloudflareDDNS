import os
from ddns.logger import logger


IP_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'ip.txt')

def get_last_ip(file_path=IP_FILE):
    try:
        with open(file_path, "r") as file:
            ip = file.read().strip()
            logger.info(f"Último IP lido: {ip}")
            return ip
    except FileNotFoundError:
        logger.warning("Arquivo de IP não encontrado. Criando um novo.")
        with open(file_path, "w") as file:
            file.write("")
        return None

def save_ip(ip, file_path=IP_FILE):
    with open(file_path, "w") as file:
        file.write(ip)
    logger.info(f"Novo IP salvo: {ip}")