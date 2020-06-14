import requests
kv = {'user-agent': 'Mozilla/5.0'}

def getHTML(url):
    try:
        r = requests.get(url, timeout=10, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


if __name__ == "__main__":
    url = "https://item.jd.com/100011199522.html"
    print(getHTML(url))
