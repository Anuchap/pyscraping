import requests
from bs4 import BeautifulSoup


page = requests.get('https://skype.postjung.com/')
soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find_all('tr', class_='xw')

myfile = open('out.txt', 'w', encoding='utf-8')
for row in rows:
    email = row.find('td', class_='x1').find_all('a')[1].get_text()
    message = row.find('td', class_='x3').find_all('a')[0].get_text()
    age = row.find('td', class_='x4').get_text()
    sex = row.find('td', class_='x5').get_text()
    province = row.find('td', class_='x6').get_text()
    myfile.write('%s %s %s %s %s\n' % (email, message, age, sex, province))

myfile.close()