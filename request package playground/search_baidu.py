import requests

headers = {'user-agent': 'Mozilla/5.0'}

def search_baidu(key_words):
    try:
        kv = {'wd': "Python"}

        r = requests.get("http://baidu.com/s", params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
    except:
        return "An error has been occured"


if __name__ == '__main__':
    search_baidu("Python")
