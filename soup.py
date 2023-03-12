from bs4 import BeautifulSoup

if __name__ == '__main__':
    # simple_html = '<html><body><p>Это самый простой HTML!</p></body></html>'
    # soup = BeautifulSoup(simple_html, features='html.parser')
    price_html = """
    <table cellspacing="0" cellpadding="0" border="1">
      <tbody>
        <tr class="even_row">
          <th><p>№ п/п</p></th>
          <th class="armor"><p>Название</p></th>
          <th class="price"><p>Цена</p><p>рублей</p></th>
        </tr>
        <tr class="odd_row">
          <td><p>1.</p></td>
          <td class="armor"><p>Щит</p></td>
          <td class="price"><p>375</p></td>
        </tr>
        <tr class="even_row">
          <td><p>2.</p></td>
          <td class="armor"><p>Шлем</p></td>
          <td class="price"><p>297</p></td>
        </tr>
        <tr class="odd_row">
          <td><p>3.</p></td>
          <td class="armor"><p>Кольчуга</p></td>
          <td class="price"><p>565</p></td>
        </tr>
        <tr class="even_row">
          <td><p>4.</p></td>
          <td class="armor"><p>Булава</p></td>
          <td class="price"><p>1992</p></td>
        </tr>
        <!-- Сюда может добавиться неизвестное количество элементов экипировки.
          Их тоже нужно учитывать при расчёте средней цены. -->
      </tbody>
    </table>
    """
    soup = BeautifulSoup(price_html, 'lxml')
    # Поиск в коде всех тегов <b>.
    # result = soup.find_all('b')

    # Поиск в коде всех тегов <title> и <b>.
    # result = soup.find_all(['title', 'b'])

    # Поиск в коде всех элементов с классом 'title'.
    # result = soup.find_all(attrs={'class': 'title'})

    # Поиск в коде всех элементов <a class='hero'>.
    result = soup.find_all('td', attrs={'class': 'price'})
    a = len(result)
    b = 0
    for i in range(len(result)):
        b += int(result[i].p.text)

    print(a, b / a, result)

