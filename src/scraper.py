from bs4 import BeautifulSoup
import requests

class HomeScraper():

    def __init__(self):
        self.url = "https://www.fotocasa.es/es/"
    

    
    def scrape(self):
        print ("Web Scraping of houses data from " + "'" + self.url + "'...")
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'lxml')
        aTitle=soup.title.string
        print (aTitle)
        page=soup.prettify()
        #print (page)
        a = soup.a
        modalCookies = 'sui-MoleculeModal is-static is-MoleculeModal-open'
        # Extraer el contenido de la etiqueta con la clase 'sui-MoleculeModal is-static is-MoleculeModal-open' 
        cookies = soup.find(modalCookies)#.text.strip()
        # delete the child element
        cookies.replaceWith('')
        print (cookies)