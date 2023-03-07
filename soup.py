from bs4 import BeautifulSoup

if __name__ == '__main__':
    # simple_html = '<html><body><p>Это самый простой HTML!</p></body></html>'
    # soup = BeautifulSoup(simple_html, features='html.parser')
    html_doc = """
    <html>
      <head><title>Сказка о трёх богатырях</title></head>
      <body>
        <p class="title"><b>Сказка о трёх богатырях</b></p>

        <p class="story">
          Давным-давно жили-были три богатыря:
          <a href="http://example.com/ilya" class="hero" id="link1">Илья Муромец</a>,
          <a href="http://example.com/alesha" class="hero" id="link2">Алёша Попович</a> и
          <a href="http://example.com/dobrynya" class="hero" id="link3">Добрыня Никитич</a>.
        </p>

        <p class="story">
          И был у них один противник
          <a href="http://example.com/dragon" class="antihero" id="link4">Змей Горыныч</a>.
        </p>

        <p class="story" name="end">
          Вот и сказке конец, а кто слушал — молодец!
        </p>
      </body>
    </html>
    """
    soup = BeautifulSoup(html_doc, 'lxml')
    # Поиск в коде всех тегов <b>.
    # result = soup.find_all('b')

    # Поиск в коде всех тегов <title> и <b>.
    # result = soup.find_all(['title', 'b'])

    # Поиск в коде всех элементов с классом 'title'.
    # result = soup.find_all(attrs={'class': 'title'})

    # Поиск в коде всех элементов <a class='hero'>.
    result = soup.find('a', attrs={'class': 'hero'})

    print(result['href'])

