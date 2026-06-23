import requests
from bs4 import BeautifulSoup

url = "https://mapleplanet.co.kr/board/update"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find_all("a", href=True)[:100]:
    print("TEXT:", a.get_text(strip=True))
    print("LINK:", a["href"])
    print("-" * 50)
