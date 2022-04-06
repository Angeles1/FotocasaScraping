from asyncio.windows_events import NULL
from collections import defaultdict
from typing import OrderedDict
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from fcScrapper import datasetGeneration
import traceback

class FcScrapper:

    n_pages = 1
    url= 'https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l'
    webdriver_path= 'webdriver/chromedriver.exe'

    def __init__(self, n_pages=n_pages, url=url, executable_path=webdriver_path):
        self.n_pages = n_pages
        self.url = url
        self.browser = webdriver.Chrome(executable_path)
        self.open_browser()

    def __del__(self):
        self.close_browser()

    def open_browser(self):
        self.browser.get(self.url)

    def close_browser(self):
        self.browser.quit()


    def accept_cookies(self):
        div_selector = "div.sui-MoleculeModal-dialog"
        button_selector = "button.sui-AtomButton[data-testid=TcfAccept]"
        css_selector = div_selector + " " + button_selector

        accept_button = self.browser.find_elements(by=By.CSS_SELECTOR,
                                                   value= css_selector)
        if len(accept_button) == 1:
            accept_button[0].click()
        return

    def scrap_pages(self):
        self.scrap_page()
        time.sleep(3)
        print ("timer")
        if self.n_pages > 1:
            for i in range(2, self.n_pages+1):
                print("Index: " + str(i))
                new_url = self.url + "/" + str(i)
                self.browser.get(new_url)
                self.scrap_page()
                #self.scrap_page_clicking()

    def scrap_page(self):
        # Pending -> Do not clic
        
        self.accept_cookies()
        self.scroll_to_bottom()
        article_selector = "section.re-SearchResult>article"
        searchs = self.browser.find_elements(by=By.CSS_SELECTOR,
                                             value=article_selector)

        for search in searchs:
            title = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardTitle")
            title = title.text.replace("Piso en ", "")
            if "," in title:
                title = title.split(", ")[-1]
            price = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardPrice")
            price = price.text.split(" ")
            price = price[0].replace(".", "")                  
            try:
                number_of_bedrooms = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardFeaturesWithIcons-feature-icon--rooms").text
                number_of_bedrooms = number_of_bedrooms.split(" ")
                number_of_bedrooms = number_of_bedrooms[0]
            except selenium.common.exceptions.NoSuchElementException:
                features_simple = search.find_elements(by=By.CSS_SELECTOR,
                                                          value="ul.re-CardFeatures-wrapper>li")
                if len(features_simple) > 0:
                    number_of_bedrooms = features_simple[0].text
                    number_of_bedrooms = number_of_bedrooms.split(" ")
                    number_of_bedrooms = number_of_bedrooms[0]
                else:
                    number_of_bedrooms = 'NA'
                
            try:
                dimension = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardFeaturesWithIcons-feature-icon--surface").text
                dimension = dimension.split(" ")
                dimension = dimension[0]                        
            except selenium.common.exceptions.NoSuchElementException:
                features_simple = search.find_elements(by=By.CSS_SELECTOR,
                                                          value="ul.re-CardFeatures-wrapper>li")
                if len(features_simple) > 2:
                    dimension = features_simple[2].text
                    dimension = dimension.split(" ")
                    dimension = dimension[0]  
                else:
                    dimension = 'NA'
            
            try:
                floor = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardFeaturesWithIcons-feature-icon--floor").text
                floor = floor.split(" ")
                floor = floor[0]
            except selenium.common.exceptions.NoSuchElementException:
                features_simple = search.find_elements(by=By.CSS_SELECTOR,
                                                          value="ul.re-CardFeatures-wrapper>li")
                if len(features_simple) > 3:
                    floor = features_simple[3].text
                    floor = floor.split(" ")
                    floor = floor[0]
                else:
                    floor = 'NA'
            
            try:
                number_of_bathrooms = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardFeaturesWithIcons-feature-icon--bathrooms").text
                number_of_bathrooms = number_of_bathrooms.split(" ")
                number_of_bathrooms = number_of_bathrooms[0]
                print(number_of_bathrooms)

            except selenium.common.exceptions.NoSuchElementException:
                features_simple = search.find_elements(by=By.CSS_SELECTOR,
                                                          value="ul.re-CardFeatures-wrapper>li")
                if len(features_simple) > 1:
                    number_of_bathrooms = features_simple[1].text
                    number_of_bathrooms = number_of_bathrooms.split(" ")
                    number_of_bathrooms = number_of_bathrooms[0]
                    print(number_of_bathrooms)
                else:
                    number_of_bathrooms = 'NA'

            try:
                link_search = search.find_elements(by=By.TAG_NAME, value="a")[0].get_attribute("href")
                ref_number = link_search.split('/')[-2]
            except selenium.common.exceptions.NoSuchElementException:
                link_search = 'NA'
                ref_number = 'NA'
            
            #print(title.text)
            #print(price.text)
            #print(number_of_bedrooms)
            #print(dimension)
            #print(floor)
            #print(number_of_bathrooms)
            #print(link_search)
            
            card_scraped = OrderedDict()
            card_scraped['ID'] = 1
            card_scraped['ref_number'] = ref_number
            card_scraped['price'] = price
            card_scraped['location'] = title
            card_scraped['city'] = 'Barcelona'
            card_scraped['number_of_bedrooms'] = number_of_bedrooms
            card_scraped['number_of_bathrooms'] = number_of_bathrooms
            card_scraped['dimension'] = dimension
            card_scraped['floor'] = floor
            card_scraped['source'] = 'Fotocasa'
            card_scraped['Link'] = link_search
            


            datasetGeneration.datasetGeneration.GenerateDataset(card_scraped)

        print(len(searchs))


    def scrap_page_clicking(self):
        self.accept_cookies()
        counter = 1

        while True:
            time.sleep(3)

            self.scroll_to_bottom()
            article_selector = "article.re-CardPackPremium"
            cards = self.browser.find_elements(by=By.CSS_SELECTOR,
                                             value=article_selector)
            if(counter > len(cards)):
                break
            card = cards[counter-1]
            
            card.click()
            dict_result = self.scrap_card()
            print(dict_result)
            datasetGeneration.datasetGeneration.GenerateDataset(dict_result)  
            counter += 1
            

    def scrap_card(self):
        time.sleep(3)
        card_info = {}

        # Source
        card_info['source'] = "fotocasa"

        # Id
        card_info['id'] = self.browser.current_url.split('/')[-2]

        # Price
        price_selector = "span.re-DetailHeader-price"
        price_elem = self.browser.find_element(by=By.CSS_SELECTOR,
                                             value=price_selector)
        card_info['price'] = price_elem.text.split()[0]
        print("Price: " + card_info['price'])

        #Location
        title_selector = "h1.re-DetailHeader-propertyTitle"
        title_elem = self.browser.find_element(by=By.CSS_SELECTOR,
                                             value=title_selector)
        card_info['location'] = title_elem.text
        print("Location: " +  card_info['location'])

        #Bedrooms
        features_selector = "ul.re-DetailHeader-features " \
                            "li.re-DetailHeader-featuresItem"
        features = self.browser.find_elements(by=By.CSS_SELECTOR,
                                              value=features_selector)
        try:
            bedroom_text = features[0].find_elements(by=By.TAG_NAME,
                                                 value="span")
            card_info['number_of_bedrooms'] = bedroom_text[-1].text
        except IndexError:
             card_info['number_of_bedrooms'] = 'NA'
        print(card_info['number_of_bedrooms'])

        #Dimension

        try:
            dimension_text = features[2].find_elements(by=By.TAG_NAME,
                                                 value="span")
            card_info['dimension'] = dimension_text[-1].text
        except IndexError:
            card_info['dimension'] = "NA"
        print("Dimension: " + card_info['dimension'])

        #Floors
        try:
            floor_text = features[3].find_elements(by=By.TAG_NAME,
                                                   value="span")
            card_info['floor'] = floor_text[-1].text
        except IndexError:
            card_info['floor'] = 0
        print("Floor: " + str(card_info['floor']))

        #Type
        detailed_info_selector = "section.sui-SectionInfo"
        detailed_info = self.browser.find_elements(by=By.CSS_SELECTOR,
                                                    value=detailed_info_selector)[1]
        detailed_list_selector = "div.sui-SectionInfo-content>div>div.re-DetailFeaturesList\
        >div.re-DetailFeaturesList-feature"
        detailed_info_list = detailed_info.find_elements(by=By.CSS_SELECTOR,
                                                        value=detailed_list_selector)
        # Other details
        for detail in detailed_info_list:
            details_to_extract = ["Tipo de immueble", "Estado", "Antigüedad",
            "Amueblado", "Consumo de energia", "Emisiones"]
        
            content_selector = "div.re-DetailFeaturesList-featureContent"
            label_selector = "p.re-DetailFeaturesList-featureLabel"
            value_selector = "p.re-DetailFeaturesList-featureValue"
            content = detail.find_element(by=By.CSS_SELECTOR,
                                          value=content_selector)
            label = content.find_element(by=By.CSS_SELECTOR,
                                        value=label_selector).text
            
            if label in details_to_extract:
                value = content.find_element(by=By.CSS_SELECTOR,
                                            value=value_selector)
                print("Label: " + label)
                print("Value: " + value.text)
                card_info[label] = str(value.text)
                print("Dict value: " + card_info[label])
 
        #Finish -> go back
        self.browser.back()
        time.sleep(3)
        return card_info

    def scroll_to_pos(self, pos):
        print(pos)
        self.browser.execute_script("window.scrollTo(0, " + str(pos) + ");")

    def scroll_to_element(self, element):
        pass

    def scroll_to_top(self):
        self.browser.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        counter = 0
        windows_height = self.browser.get_window_size()['height']

        while True:
            page_nav = self.browser.find_elements(by=By.CSS_SELECTOR,
                                                  value="div.re-Pagination")
            scroll_to = windows_height*counter
            if self.is_end_page() or self.is_max_scroll(scroll_to):
                break
            counter += 1
            self.browser.execute_script(
                    "window.scrollTo(0, " + str(windows_height*counter) + ");")

    def is_end_page(self):
        try:
            page_nav = self.browser.find_elements(by=By.CSS_SELECTOR,
                                              value="div.re-Pagination")
            return len(page_nav) != 0
        except: 
            traceback.print_exc()
        
        
        
    def is_max_scroll(self, scroll_to):
        body = self.browser.find_element(by=By.TAG_NAME, value="body")
        max_scroll = body.size['height']
        return scroll_to > max_scroll

