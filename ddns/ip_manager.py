import os


IP_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'ip.txt')


def get_last_ip(file_path=IP_FILE):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write("")
        return None

def save_ip(ip, file_path=IP_FILE):
    with open(file_path, "w") as file:
        file.write(ip)