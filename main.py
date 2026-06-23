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

try:
    r = scraper.get(url)

    if r.status_code != 200:
        print(f"접속 실패: {r.status_code}")
        exit()

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
            "content": "🍁 **신규 패치노트 발견!**",
            "embeds": [
                {
                    "title": post_title,
                    "url": post_url,
                    "description": "📖 클릭하여 패치노트를 확인하세요.",
                    "color": 16753920,
                    "fields": [
                        {
                            "name": "📌 상태",
                            "value": "신규 패치노트 등록",
                            "inline": True
                        },
                        {
                            "name": "🔗 링크",
                            "value": f"[바로가기]({post_url})",
                            "inline": True
                        }
                    ],
                    "footer": {
                        "text": "메이플플래닛 자동 패치 알림"
                    }
                }
            ]
        }

        response = requests.post(WEBHOOK_URL, json=payload)

        print("디스코드 전송:", response.status_code)

        with open(LAST_FILE, "w", encoding="utf-8") as f:
            f.write(post_url)

    else:
        print("신규 패치노트 없음")

except Exception as e:
    print("오류 발생:", str(e))
