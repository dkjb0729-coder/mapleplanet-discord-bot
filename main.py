import cloudscraper
import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

scraper = cloudscraper.create_scraper(
    browser={
        "browser": "chrome",
        "platform": "windows",
        "mobile": False
    }
)

url = "https://mapleplanet.co.kr/board/update"

r = scraper.get(url)

print("상태코드:", r.status_code)
print("응답길이:", len(r.text))

requests.post(
    WEBHOOK_URL,
    json={
        "content": f"상태코드: {r.status_code}\n응답길이: {len(r.text)}\n\n```{r.text[:1000]}```"
    }
)

print("전송 완료")
