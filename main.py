import requests

url = "https://mapleplanet.co.kr/board/update"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://mapleplanet.co.kr/"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text[:500])
