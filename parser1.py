import requests

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator as GT


url = 'https://scrapingclub.com/exercise/list_basic/'
params = {
    'page': 1,
    }

pages = 2
n = 1
x=1

def f():
    def translate(text, target='ru', source='auto'):
        return GT(source=source, target=target).translate(text)
    global d, x
    
    for n, i in enumerate(items, start=1):
        item_name = i.find('h4', class_='card-title').text.strip()
        item_price = i.find('h5').text
        url = d[n-1]
        response = requests.get('https://scrapingclub.com' + url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find('p', class_='card-text').text.strip()
        text = translate(text)
        print(f'{x}: Название: {item_name}\n Цена: {item_price}\n Описание: {text}')
        x+=1

while params['page'] <= pages:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_ = 'col-lg-4 col-md-6 mb-4')
    div = soup.find_all("div", class_="card")
    d = [i.a.get("href") for i in div]
    f()
    last_page_num = int(soup.find_all('a', class_='page-link')[-2].text)
    pages = last_page_num if pages < last_page_num else pages
    params['page'] += 1
