import requests
from bs4 import BeautifulSoup

try:
    r = requests.get("https://python123.io/ws/demo.html")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text

    soup = BeautifulSoup(demo, "html.parser")

    for link in soup.find_all('a'):
        print(link.get("href"))

except:
    print("An Error Has Been Occured")
