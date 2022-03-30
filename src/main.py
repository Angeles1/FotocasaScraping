from scraper import HomeScraper
from bs4 import BeautifulSoup
import requests

#scraper = HomeScraper();
#scraper.scrape();
url = "https://www.fotocasa.es/es/"

print ("Web Scraping of houses data from " + "'" + url + "'...")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
aTitle=soup.title.string
print (aTitle)
page=soup.prettify()
#print (page)
a = soup.a
modalCookies = 're-SharedCmp'
# Extraer el contenido de la etiqueta con la clase 're-SharedCmp' 
cookies = soup.find(class_=modalCookies)
# delete the child element
cookies.decompose()
#print (cookies)
print (page)
with open('readme.txt', 'w') as f:
    f.write(page)