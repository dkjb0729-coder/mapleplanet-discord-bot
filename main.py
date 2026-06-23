import requests
from bs4 import BeautifulSoup

url = "https://mapleplanet.co.kr/board/update"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find_all("a", href=True):

    href = a["href"]
    text = a.get_text(strip=True)

    if "/board/update/" in href:
        print("FOUND")
        print("TEXT=", repr(text))
        print("HREF=", repr(href))
        print("-" * 50)
