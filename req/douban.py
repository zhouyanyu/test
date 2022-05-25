import requests
from bs4 import BeautifulSoup


class Douban:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.data = []
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'}
        for item in range(0, 251, 25):
            self.data.append(item)

    def get_top_250(self):
        for start in self.data:
            start = str(start)
            html = requests.get(self.url, params={'start': start}, headers=self.header)
            db = BeautifulSoup(html.text, 'html.parser')
            top_250_name = db.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
            for singel_name in top_250_name:
                print(singel_name.get_text())

if __name__ == "__main__":
    this_db = Douban()
    this_db.get_top_250()