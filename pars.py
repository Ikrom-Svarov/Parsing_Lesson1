import requests
from bs4 import BeautifulSoup
import json

link = 'https://auto.drom.ru/'
response = requests.get(link).text

soup = BeautifulSoup(response, 'lxml')

#сначало парсим блок всей страници где начодятся все записи товаров с ценой и описанием
block = soup.find('div',class_="css-1173kvb eojktn00")
with open ('block.txt', 'w') as f:
    f.write(str(block.text))
# потом в нутри блока страници находим  тег  с ценой который относится ко всем записям(машинам) на сайте
prices = block.find_all('span', class_="css-46itwz e162wx9x0")

with open ('price.txt', 'w') as f:
    for price in prices:
      f.write(str(price.text)+ ',,,')
# потом также в нутри блока страници находим обший тег имен машин на сайте который относится ко всем машинам
names = block.find_all('div', class_="css-l1wt7n e3f4v4l2")

with open ('name.txt', 'w') as f :
    for name in names:
        f.write(str(name.text)+ ',,,')
# тоже самое здесь только ишем описание
descritions = block.find_all('div', class_="css-1fe6w6s e162wx9x0")

with open ('description.txt', 'w') as f:
    for description in descritions:
        f.write(str(description.text) + ',,,')    

# для ссылки в нутри блока ишем все теги а
links = block.find_all('a')

with open('link.txt', 'w') as f:
    for link in links:
        f.write(str(link.get('href'))+ ',,,') # и делаем запрос на все атрибуты href  в тегах а

# потом мы это все записываем в словарь 
data = {'cars': []}

for name, price, description, link in zip(names, prices, descritions, links):
    item = {'name': name.text, 'price': price.text, 'description': description.text, 'link':link.get('href')}
    data['cars'].append(item)

json_data = json.dumps(data, ensure_ascii=False, indent=4)

with open('file.txt', 'w') as f:
        f.write(json_data)

