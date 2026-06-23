import requests
from bs4 import BeautifulSoup

url = "https://mapleplanet.co.kr/board/update"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("상태:", r.status_code)

soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find_all("a", href=True)[:50]:
    print(a.get("href"))
