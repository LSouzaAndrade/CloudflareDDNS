from ddns.ip_manager import get_last_ip, save_ip
from ddns.ip_service import get_current_ip
from ddns.cloudflare_api import update_dns
from ddns.logger import logger
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    last_ip = get_last_ip()
    new_ip = get_current_ip()

    if new_ip and new_ip != last_ip:
        logger.info(f"IP mudou de {last_ip} para {new_ip}")
        if update_dns(new_ip):
            save_ip(new_ip)
    else:
        logger.info("IP não mudou ou falhou ao obter IP atual. Nenhuma ação necessária.")