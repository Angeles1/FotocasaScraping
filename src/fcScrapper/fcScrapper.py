from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fcScrapper import datasetGeneration

class FcScrapper:

    n_pages = 1
    url= 'https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l'
    webdriver_path= '../webdriver/chromedriver.exe'

    def __init__(self, n_pages=n_pages, url=url, webdriver_path=webdriver_path):
        self.n_pages = n_pages
        self.url = url
        self.webdriver_path = webdriver_path
        self.browser = webdriver.Chrome(webdriver_path)
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

    def scrap_page(self):
        # Pending -> Do not clic
        self.accept_cookies()
        self.scroll_to_bottom()

        article_selector = "article.re-CardPackPremium"
        searchs = self.browser.find_elements(by=By.CSS_SELECTOR,
                                             value=article_selector)
        for search in searchs:
            title = search.find_element(by=By.CSS_SELECTOR,
                                        value="span.re-CardTitle ")
            print(title.text)
        print(len(searchs))

    def scrap_page_clicking(self):
        self.accept_cookies()
        counter = 1

        while True:
            time.sleep(3)
            article_selector = "article.re-CardPackPremium"
            card = self.browser.find_elements(by=By.CSS_SELECTOR,
                                             value=article_selector)[counter-1]
            scroll_to = card.size['height'] + card.location['y']
            card.click()
            dict_result = self.scrap_card()
            print(dict_result)
            datasetGeneration.datasetGeneration.GenerateDataset(dict_result)
            #print ("#######GENERANDO DATASET")
            #break
            if self.is_end_page():
                break
            self.scroll_to_pos(scroll_to)
            counter += 1


    def scrap_card(self):
        time.sleep(3)
        card_info = {}

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
        card_info['location'] = title_elem.text.split(',')[-1].lstrip()
        print("Location: " +  card_info['location'])

        #Bedrooms
        features_selector = "ul.re-DetailHeader-features " \
                            "li.re-DetailHeader-featuresItem"
        features = self.browser.find_elements(by=By.CSS_SELECTOR,
                                              value=features_selector)
        bedroom_text = features[0].find_elements(by=By.TAG_NAME,
                                                 value="span")
        card_info['number_of_bedrooms'] = bedroom_text[-1].text
        print(card_info['number_of_bedrooms'])
        #Dimension

        dimension_text = features[2].find_elements(by=By.TAG_NAME,
                                                 value="span")
        card_info['dimension'] = dimension_text[-1].text
        print("Dimension: " + card_info['dimension'])
        #Floors
        floor_text = features[3].find_elements(by=By.TAG_NAME,
                                                   value="span")
        card_info['floor'] = floor_text[-1].text
        print("Floor: " + card_info['floor'])




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
        page_nav = self.browser.find_elements(by=By.CSS_SELECTOR,
                                              value="div.re-Pagination")
        return len(page_nav) != 0

    def is_max_scroll(self, scroll_to):
        body = self.browser.find_element(by=By.TAG_NAME, value="body")
        max_scroll = body.size['height']
        return scroll_to > max_scroll

    def go_next_page(self):
        pass

