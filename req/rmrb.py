import requests as req
from bs4 import BeautifulSoup
from datetime import datetime
import fitz
import os

class Rmrb:
    def __init__(self):
        self.today = datetime.now().strftime('%y-%m/%d')
        self.today_ = datetime.now().strftime('%y%m%d')
        self.rm_url = 'http://paper.people.com.cn/rmrb/images/20' + self.today + '/01/rmrb20' + self.today_ + '01.pdf'
        self.xh_url = 'http://mrdx.cn/PDF/20' + self.today_ + '/01.pdf'
        self.pdf_path = "req/pdf/" + self.today_ + "01.pdf"
        if not os.path.exists("req/pdf"):
            os.makedirs("req/pdf")
    def get_pdf(self, uri, typ):
        my_pdf = req.get(uri)
        with open(self.pdf_path, mode='wb') as f:
            f.write(my_pdf.content)
        pdfDoc = fitz.open(self.pdf_path)
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 2  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 2
        
        mat = fitz.Matrix(zoom_x,zoom_y).prerotate(rotate)
        pix = pdfDoc[0].get_pixmap(matrix=mat, alpha=False)
        pix.save("req/pdf/" + self.today_ + typ + '.png')

if __name__ == "__main__":
    rm = Rmrb()
    rm.get_pdf(rm.xh_url,'xh')