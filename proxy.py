import requests
import random

def check_proxy(proxy):
    try:
        response = requests.get('https://www.example.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Прокси {proxy} работает")
    except:
        print(f"Прокси {proxy} не работает")

def scan_proxies(num_proxies):
    for _ in range(num_proxies):
        proxy = get_random_proxy()
        check_proxy(proxy)

def get_random_proxy():
    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    port = random.randint(1000, 9999)
    return f"http://{ip}:{port}"

# Количество прокси-серверов для сканирования
num_proxies = 1000

scan_proxies(num_proxies)
