import requests
from bs4 import BeautifulSoup

url = "https://mapleplanet.co.kr/board/update"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("접속 시작")

response = requests.get(url, headers=headers)

print("상태코드:", response.status_code)
print("응답 길이:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

print("링크 검색 시작")

count = 0

for a in soup.find_all("a", href=True):
    text = a.get_text(strip=True)
    href = a["href"]

    print("TEXT:", text)
    print("LINK:", href)
    print("-" * 50)

    count += 1

    if count >= 50:
        break

print("총 출력:", count)
print("테스트 완료")
