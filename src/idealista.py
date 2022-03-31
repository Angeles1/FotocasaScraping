import glob
import os
import string
import requests

def getAccessToken():
    url = "https://api.idealista.com/oauth/token?grant_type=client_credentials"

    payload={}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'Basic Z3JxdWNzNmhoZDR4bjJmMHRoeWM5NGQ1NjdtcjV1cHk6ZlNPeGFkOXhIUTdx'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = response.json()['access_token']
    print(access_token)

def configureFilters():
    url = "https://api.idealista.com/3.5/es/search?propertyType=homes&operation=rent&center=41.385063,2.173404&distance=15000"

    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIl0sImV4cCI6MTY0ODgwMTc0NiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QVUJMSUMiXSwianRpIjoiYjVlMjJiNmMtYzgxMS00YTM3LWIwOGYtM2MxZWFlN2Q2MjY0IiwiY2xpZW50X2lkIjoiZ3JxdWNzNmhoZDR4bjJmMHRoeWM5NGQ1NjdtcjV1cHkifQ.HWksC84ITifM4FDqaWz7WpnoJhGVHk1IM7-tXUAybws'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    totalPages = response.json()['totalPages']
    print(totalPages)
    return totalPages
def getItemPerPage(totalPages):
    #TODO recorrer cada página y guardar datos de interés
    url = "https://api.idealista.com/3.5/es/search?propertyType=homes&operation=rent&center=41.385063,2.173404&distance=15000&numPage="+str(totalPages)

    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIl0sImV4cCI6MTY0ODgwMTc0NiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QVUJMSUMiXSwianRpIjoiYjVlMjJiNmMtYzgxMS00YTM3LWIwOGYtM2MxZWFlN2Q2MjY0IiwiY2xpZW50X2lkIjoiZ3JxdWNzNmhoZDR4bjJmMHRoeWM5NGQ1NjdtcjV1cHkifQ.HWksC84ITifM4FDqaWz7WpnoJhGVHk1IM7-tXUAybws'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.json()['totalPages']
    print(result)

totalPages = getAccessToken()
configureFilters()
getItemPerPage(totalPages)