#!/usr/bin/env python

import requests
import argparse
import getCategoryInfo
from bs4 import BeautifulSoup


# url = "http://books.toscrape.com/index.html"
def main(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    categories_name = [el.text.strip() for el in soup.select("ul > li > ul > li > a")]
    categories_url = ["http://books.toscrape.com/"+el["href"] for el in soup.select("ul > li > ul > li > a")]


    if len(categories_name) == len(categories_url):
        for i in range(len(categories_url)):
            print("Scrapping en cours de la catégorie :" + categories_name[i])
            print("______________________________________________")
            getCategoryInfo.main(categories_url[i], categories_name[i])



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Enter a valid website url, default is http://books.toscrape.com/index.html", default="http://books.toscrape.com/index.html")
    args = parser.parse_args()

    try:
        main(args.url)
    except :
        print("Error : add a valid website url as an argument")