import requests
from bs4 import BeautifulSoup

try:
    r = requests.get("https://python123.io/ws/demo.html")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text

    soup = BeautifulSoup(demo, "html.parser")
    print("The soup is: ", soup, "\n")
    # print("The title is: ", soup.title, "\n")
    # tag = soup.a
    # print("tag a of soup is: ", tag)
    print(soup.head.contents)
except:
    print("An Error Has Been Occured")
