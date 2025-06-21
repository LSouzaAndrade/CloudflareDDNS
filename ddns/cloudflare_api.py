import os
import requests
from ddns.logger import logger


def update_dns(new_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{os.getenv('CLOUDFLARE_ZONE_ID')}/dns_records/{os.getenv('CLOUDFLARE_RECORD_ID')}"
    payload = {
        "type": "A",
        "name": os.getenv('CLOUDFLARE_RECORD_NAME'),
        "content": new_ip,
        "ttl": 120,
        "proxied": False
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('CLOUDFLARE_API_TOKEN')}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        logger.info(f"DNS atualizado com sucesso para o IP {new_ip}")
        return True
    except requests.RequestException as e:
        logger.error(f"Erro ao atualizar o DNS: {e}")
        return False
