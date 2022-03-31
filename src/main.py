import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from fcScrapper import fcScrapper

URL = 'https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l'
PATH = 'webdriver/chromedriver.exe'

scrapper = fcScrapper.FcScrapper(1, URL, PATH)
scrapper.scrap_page_clicking()
input()
scrapper.close_browser()