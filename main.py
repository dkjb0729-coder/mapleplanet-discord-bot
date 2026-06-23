import cloudscraper
import requests
from bs4 import BeautifulSoup
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

LAST_FILE = "last_post.txt"

scraper = cloudscraper.create_scraper(
    browser={
        "browser": "chrome",
        "platform": "windows",
        "mobile": False
    }
)

url = "https://mapleplanet.co.kr/board/update"

r = scraper.get(url)

soup = BeautifulSoup(r.text, "html.parser")

post_title = None
post_url = None

for a in soup.find_all("a", href=True):

    href = a["href"]
    text = a.get_text(strip=True)

    if href.startswith("/board/update/"):

        post_title = text
        post_url = "https://mapleplanet.co.kr" + href
        break

if not post_url:
    print("패치노트 찾기 실패")
    exit()

print("최신글:", post_title)
print("링크:", post_url)

last_post = ""

if os.path.exists(LAST_FILE):
    with open(LAST_FILE, "r", encoding="utf-8") as f:
        last_post = f.read().strip()

if post_url != last_post:

    payload = {
        "content": f"🍁 **신규 패치노트 발견!**\n\n📢 {post_title}\n{post_url}"
    }

    requests.post(WEBHOOK_URL, json=payload)

    with open(LAST_FILE, "w", encoding="utf-8") as f:
        f.write(post_url)

    print("디스코드 전송 완료")

else:
    print("신규 패치노트 없음")
