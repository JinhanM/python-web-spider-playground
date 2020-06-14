import requests

url = "https://www.ip138.com/iplookup.asp?ip="
action = "&action=2"
kv = {'user-agent': 'Mozilla/5.0'}

try:
    r = requests.get("https://www.ip138.com/iplookup.asp?ip=38.39.232.172&action=2", headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("there is an error has been ocurred")
