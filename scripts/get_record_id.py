from dotenv import load_dotenv
import os
import requests


if __name__ == "__main__":
    load_dotenv()

    RECORD_INFO_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'records_info.txt')

    url = f"https://api.cloudflare.com/client/v4/zones/{os.getenv('CLOUDFLARE_ZONE_ID')}/dns_records"
    headers = {
        "Authorization": f"Bearer {os.getenv('CLOUDFLARE_API_TOKEN')}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(RECORD_INFO_FILE, "w") as file:
            file.write(response.text)
        print("Solicitação bem-sucedida. Dados salvos em", RECORD_INFO_FILE)
    except requests.RequestException as e:
        print(f"Erro na solicitação: {e}")
