import requests
import bs4
import lxml

res = requests.get('https://en.wikipedia.org/wiki/Cicada_3301')
soup = bs4.BeautifulSoup(res.text, 'lxml')
image_info = soup.select('.thumbimage')
cicada = image_info[0]
print(cicada['src'])
cicada_image_link = 'http:'+cicada['src']
print(cicada_image_link)

res2 = requests.get(cicada_image_link, 'lxml')
soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
print(soup2)
f = open('cicada_new.jpg', 'wb')
f.write(res2.content)
f.close
