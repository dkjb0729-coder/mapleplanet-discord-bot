import requests
from bs4 import BeautifulSoup
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

URL = "https://mapleplanet.co.kr/board/update"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

print("상태코드:", response.status_code)
print("URL:", response.url)
print("응답길이:", len(response.text))

payload = {
    "content": f"✅ GitHub Actions 테스트 성공\n상태코드: {response.status_code}"
}

requests.post(WEBHOOK_URL, json=payload)

print("웹훅 전송 완료")
