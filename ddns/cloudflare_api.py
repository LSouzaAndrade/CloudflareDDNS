import os
import requests

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
        return True
    except requests.RequestException:
        return False