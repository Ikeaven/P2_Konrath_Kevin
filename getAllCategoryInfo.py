#!/usr/bin/env python

import requests
import getCategoryInfo
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

categories_name = [el.text.strip() for el in soup.select("ul > li > ul > li > a")]
categories_url = ["http://books.toscrape.com/"+el["href"] for el in soup.select("ul > li > ul > li > a")]


if len(categories_name) == len(categories_url):
    for i in range(len(categories_url)):
        

        print("Scrapping en cours de la catégorie :" + categories_name[i])
        print("______________________________________________")
        getCategoryInfo.main(categories_url[i], categories_name[i])

