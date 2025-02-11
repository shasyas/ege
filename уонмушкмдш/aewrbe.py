import beautifulsoup4

soup = BeautifulSoup('<html><head><title>Заголовок страницы</title></head><body></body></html>', 'html.parser')

# Получаем тег body и добавляем в него параграф
soup.body.append(soup.new_tag('p', id='intro'))
soup.body.p.string = 'Добро пожаловать на мою страницу!'

print(soup.prettify())