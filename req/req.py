"""练习requests"""
import requests as req

ver = req.__version__
cpr = req.__copyright__


resp = req.request(method='GET', url='http://www.webcode.me')
with open('req/web.html', mode='w',encoding='utf-8') as f:
    f.write(resp.text)

print('好了')