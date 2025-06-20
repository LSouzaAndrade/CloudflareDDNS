from ddns.ip_manager import get_last_ip, save_ip
from ddns.ip_service import get_current_ip
from ddns.cloudflare_api import update_dns
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    last_ip = get_last_ip()
    new_ip = get_current_ip()

    if new_ip and new_ip != last_ip:
        if update_dns(new_ip):
            save_ip(new_ip)