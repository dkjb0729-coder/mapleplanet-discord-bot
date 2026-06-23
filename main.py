import requests
from bs4 import BeautifulSoup
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

url = "https://mapleplanet.co.kr/board/update"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

msg = r.text[:1800]

requests.post(
    WEBHOOK_URL,
    json={
        "content": f"```{msg}```"
    }
)

print("완료")
