import requests
from ddns.logger import logger


def get_current_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip = response.json().get("ip")
        logger.info(f"IP atual obtido: {ip}")
        return ip
    except requests.RequestException as e:
        logger.error(f"Erro ao obter o IP atual: {e}")
        return None