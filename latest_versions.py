import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import re


MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'
    # Создание "супа".
    soup = BeautifulSoup(response.text, features='lxml')
    sidebar = soup.find('div', attrs={'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')
    # Перебор в цикле всех найденных списков.
    for ul in ul_tags:
        # Проверка, есть ли искомый текст в содержимом тега.
        if 'All versions' in ul.text:
            # Если текст найден, ищутся все теги <a> в этом списке.
            a_tags = ul.find_all('a')
            # Остановка перебора списков.
            break
    # Если нужный список не нашёлся,
    # вызывается исключение и выполнение программы прерывается.
    else:
        raise Exception('Ничего не нашлось')
    # Список для хранения результатов.
    results = []
    # Шаблон для поиска версии и статуса:
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    # Цикл для перебора тегов <a>, полученных ранее.
    for a_tag in a_tags:
        # Напишите новый код, ориентируясь на план.
        link = a_tag['href']
        text_match = re.search(pattern, a_tag.text)
        if text_match:
            version = text_match.group('version')
            status = text_match.group('status')
            results.append(
                (link, version, status)
            )
        else:
            results.append(
                (link, a_tag.text)
            )

    # Печать результата.
    for row in results:
        print(*row)
