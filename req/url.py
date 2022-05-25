from urllib.request import urlopen

moni_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

url = 'http://www.baidu.com/'
resp = urlopen(url)

with open('req/bd.html', mode='w') as f:
    f.write(resp.read().decode('utf-8'))

print('好了')
