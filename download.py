import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import re
# Добавьте к списку импортов импорт класса Path из модуля pathlib.
from pathlib import Path


DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
# Добавьте константу, где будет храниться путь до директории с текущим файлом.
BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    # Создание "супа".
    soup = BeautifulSoup(response.text, features='lxml')
    main_tag = soup.find('div', {'role': 'main'})
    table_tag = main_tag.find('table', {'class': 'docutils'})
    # print(table_tag.prettify())
    # Добавьте команду получения нужного тега.
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    # Сохраните в переменную содержимое атрибута href.
    pdf_a4_link = pdf_a4_tag['href']
    # Получите полную ссылку с помощью функции urljoin.
    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
    # print(archive_url)
    filename = archive_url.split('/')[-1]
    # Сформируйте путь до директории downloads.
    downloads_dir = BASE_DIR / 'downloads'
    # Создайте директорию.
    downloads_dir.mkdir(exist_ok=True)
    # Получите путь до архива, объединив имя файла с директорией.
    archive_path = downloads_dir / filename
    # Загрузка архива по ссылке.
    response = session.get(archive_url)

    # В бинарном режиме открывается файл на запись по указанному пути.
    with open(archive_path, 'wb') as file:
        # Полученный ответ записывается в файл.
        file.write(response.content)
