import requests
from bs4 import BeautifulSoup
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

url = "https://mapleplanet.co.kr/board/update"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

results = []

for a in soup.find_all("a", href=True):
    href = a["href"]
    text = a.get_text(strip=True)

    if "/board/update/" in href:
        results.append(f"{text} -> {href}")

message = "\n".join(results[:20])

requests.post(
    WEBHOOK_URL,
    json={
        "content": f"디버그 결과\n```{message[:1800]}```"
    }
)

print("전송 완료")
