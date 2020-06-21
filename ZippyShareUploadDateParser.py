from lxml import html
import requests

url = []
with open('inputZippy.txt', 'r', encoding='utf-8') as f:
    url = f.readlines()
url = [x.strip() for x in url]

my_file = open('output.txt', 'w')
my_file.write('Link' + '\t' + 'Result\n')

a = 0
b = str(len(url))
print('Получено: ' + b + ' ссылок\n')
print('Начинаем. . .')
for a in range(len(url)):
    try:
        page = requests.get(url[a])
        tree = html.fromstring(page.content)

        uplDate = tree.xpath('//*[@id="lrbox"]/div[1]/div[1]/div[1]/font[4]')
        data = (url[a] + '\t' + uplDate[0].text + '\n')
        print(f'Пройдено: {a + 1} из {len(url)}')
    except:
        dataError = (url[a] + '\t' + 'error\n')
        my_file.write(dataError)
        print(f'Пройдено: {a + 1} из {len(url)} (ошибка)')

    my_file.write(data)

print('================================')
print('Go to output.txt and see results')
print('================================')
input('Press "ENTER" to exit')
print()
