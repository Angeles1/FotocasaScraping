import glob
import os
import string
import requests
from fcScrapper import datasetGeneration
import json

def getAccessToken():
    url = "https://api.idealista.com/oauth/token?grant_type=client_credentials"

    payload={}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic SECRET'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = response.json()['access_token']
    return access_token

def configureFilters():
    url = "https://api.idealista.com/3.5/es/search?propertyType=homes&operation=rent&center=41.385063,2.173404&distance=15000"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + getAccessToken() +''
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    totalPages = response.json()['totalPages']
    print(type(totalPages)) 

    return totalPages

def getItemPerPage(totalPages):
    #TODO recorrer cada página y guardar datos de interés
    #for page_number in range(1):
    #    print(page_number)
    url = "https://api.idealista.com/3.5/es/search?propertyType=homes&operation=rent&center=41.385063,2.173404&distance=15000&numPage="+str(totalPages)

        #url = "https://api.idealista.com/3.5/es/search?propertyType=homes&operation=rent&center=41.385063,2.173404&distance=15000&numPage="+str(page_number)

    payload={}
    headers = {
        'Authorization': 'Bearer ' + getAccessToken() +''
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.json()['totalPages']
    print(result)

def generate_card(infoCard):
    card_API = {}
    card_API['ID'] = 1
    card_API['price'] = int(infoCard['price'])
    card_API['location'] = infoCard['district']
    card_API['number_of_bedrooms'] =  infoCard['rooms']
    card_API['number_of_bathrooms'] = infoCard['bathrooms']
    card_API['dimension'] = int(infoCard['size'])
    try:
        card_API['floor'] = infoCard['floor']
    except:
        card_API['floor'] = 'NA'
    card_API['source'] = 'Idealista'
    card_API['date'] = ''



    datasetGeneration.datasetGeneration.GenerateDataset(card_API)

#totalPages = getAccessToken()
#totalPages = configureFilters()
#getItemPerPage(totalPages)
json_file_path = "src/idealista.json"

with open(json_file_path, 'r', encoding="utf8") as j:
     contents = json.loads(j.read())
     #print (contents)
     #print (contents['total'])
j.close()

for infoCard in contents['elementList']:
        #print(infoCard)
        generate_card(infoCard)