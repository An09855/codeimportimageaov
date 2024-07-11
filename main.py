import requests
import unicodedata
from bs4 import BeautifulSoup

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

response = requests.get('https://lienquan.garena.vn/hoc-vien/tuong-skin/')
response2 = requests.get('https://lienquan.garena.vn/hoc-vien/tuong-skin/d/dolia/')
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('div', {'class':'st-heroes__item--img'})
for item in rows:
    yc = item.img.get('alt')
    print(item.img.get('alt'))
    print(item.img.get('src'))
    yc = yc.lower()
    yc = remove_accents(yc)
    yc = yc.replace(" ", "-").replace("đ", "d").replace("’", "")
    link = 'https://lienquan.garena.vn/hoc-vien/tuong-skin/d/' + yc + '/'
    response2 = requests.get(link)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    rows2 = soup2.find('picture')
    print(rows2.img.get('src'))