import requests
from bs4 import BeautifulSoup
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

URL = "https://mapleplanet.co.kr/board/update"
LAST_FILE = "last_post.txt"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

post_url = None
post_title = None

for a in soup.find_all("a", href=True):

    href = a["href"]
    text = a.get_text(strip=True)

    if href.startswith("/board/update/") and "패치노트" in text:

        post_url = "https://mapleplanet.co.kr" + href
        post_title = text
        break

if not post_url:
    print("최신 패치노트를 찾지 못함")
    exit()

print("최신글:", post_title)
print("링크:", post_url)

last_post = ""

if os.path.exists(LAST_FILE):
    with open(LAST_FILE, "r", encoding="utf-8") as f:
        last_post = f.read().strip()

if post_url != last_post:

    payload = {
        "content": f"🍁 신규 패치노트 발견!\n\n📢 {post_title}\n{post_url}"
    }

    r = requests.post(WEBHOOK_URL, json=payload)

    print("디스코드 전송:", r.status_code)

    with open(LAST_FILE, "w", encoding="utf-8") as f:
        f.write(post_url)

else:
    print("신규 패치노트 없음")
