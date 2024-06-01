import requests
from bs4 import BeautifulSoup as bs
import lxml

SOURCE_URL = 'https://www.python.org/downloads/source/'

response = requests.get(SOURCE_URL).text
soup = bs(response, 'lxml')
data = soup.find_all('div', {'class': 'column'})
links = []
l=[]
for column in data:
    if column.find('h2').text == 'Stable Releases':
        links = column.find_all('a')

for link in links:
    if link.text =='Gzipped source tarball':
        l.append(link.get('href'))
print(l,sep='\n')