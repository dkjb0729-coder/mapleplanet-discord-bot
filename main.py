import requests
from bs4 import BeautifulSoup
import json
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

URL = "https://mapleplanet.co.kr/board/update"
LAST_FILE = "last_post.txt"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 게시글 링크 찾기
links = soup.find_all("a", href=True)

post_url = None
post_title = None

for link in links:
    href = link["href"]

    if "/board/update/" in href:
        post_url = href
        post_title = link.get_text(strip=True)
        break

if not post_url:
    print("게시글을 찾지 못함")
    exit()

if post_url.startswith("/"):
    post_url = "https://mapleplanet.co.kr" + post_url

last_post = ""

if os.path.exists(LAST_FILE):
    with open(LAST_FILE, "r", encoding="utf-8") as f:
        last_post = f.read().strip()

if post_url != last_post:

    payload = {
        "content": f"🍁 신규 패치노트 발견!\n\n📢 {post_title}\n{post_url}"
    }

    requests.post(WEBHOOK_URL, json=payload)

    with open(LAST_FILE, "w", encoding="utf-8") as f:
        f.write(post_url)

    print("새 패치노트 전송 완료")

else:
    print("신규 패치노트 없음")
