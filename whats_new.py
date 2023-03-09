import requests_cache
from bs4 import BeautifulSoup

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # py39 = soup.find_all(id="whatsnew-index")
    py39 = soup.find_all('span', attrs={'id': 'whatsnew-index'})


    print(py39)
