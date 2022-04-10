# Práctica 1: Web scraping

## Tabla de contenido
* [Descripción](#descripcion)
* [Miembros del equipo](#miembros-del-equipo)
* [Ficheros del código fuente](#ficheros-del-codigo-fuente)
* [Recursos](#recursos)
* [Requerimientos](#requerimientos)
* [Agradecimientos](#agradecimientos)

## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web Fotocasa y de la API Idealista y generar un dataset que contiene información sobre los alquileres de la ciudad de Barcelona.

## Miembros del equipo
Esta práctica se ha desarrollado por:
* María Angeles Fuentes Expósito
* Norberto Jesús de la Cruz Falcón
## Ficheros del código fuente
* src/main.py --> fichero principal que realiza la inicialización/ejecución del programa

* src/fcScrapper/--init--.py --> por defecto

* src/fcScrapper/fcScrapper.py --> clase que realiza el web scraping de Fotocasa

* src/fcScrapper/idealista.py --> clase que realiza las peticiones a la API de Idealista

* src/fcScrapper/datasetGeneration.py --> Clase que se encarga de generar el dataset con los datos recogidos (de fcSrapper.py y de idealista.py)

* .gitignore --> Ignora ficheros a la subida del repositorio: idealistaKey.py

* idealistaKey.py --> configura el secreto de la API que nos ha dado Idealista. 

* NOTA: El fichero idealistaKey.py contiene la clave secreta de la API, que no debe ser compartida en repositorios públicos ('Authorization': 'Basic SECRET') por esta razón se incluye en .gitignore

## Recursos

* Otros webScraper de Inmobiliarias

https://github.com/EdelBlau/PEC_TPC

https://github.com/eambroa/WebScrapingFotocasa

* Ayuda con la API

https://en.wikipedia.org/wiki/Base64

https://developers.idealista.com/access-request

* Programación

https://www.geeksforgeeks.org/selenium-python-tutorial/

* Guia de estilos github

https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project

* Publicación DataSet

https://zenodo.org/record/6409838



## Requerimientos
Es necesario tener instalada la librería Selenium para ejecutar el código
```
pip install selenium
```
Para ejecutar el script también es necesario descargarse el webdriver correspondiente con la
versión de Google Chrome que se tenga instalada e incluirlo en la carpeta webdriver. El webdriver
se puede descargar desde el siguiente <a href="https://chromedriver.chromium.org/downloads">enlace</a>

## Agradecimientos
Este dataset se ha realizado gracias a la comunidad de código abierto:
* Python
* Selenium

Al repositorio y control de versiones para trabajar en equipo:
* GitHub

Y a los portales web que tienen los datos que hemos scrapeado:
* Fotocasa.es
* Idealista.com
