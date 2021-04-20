#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module extraxt all catégory, create an array with, and
    passes it to getCategoryInfo module. 
"""


import requests
# import argparse
from . import getCategoryInfo
from bs4 import BeautifulSoup, SoupStrainer


# url = "http://books.toscrape.com/index.html"
def main(url):
    """
    This function get all categories, and passes it to getCategoryInfo.py module.
    Args:
        url (str): home url of book_toscrape website
    """
    response = requests.get(url)
    only_aside = SoupStrainer("aside")
    soup = BeautifulSoup(response.content, "lxml", parse_only=only_aside)

    categories_name = [el.text.strip() for el in soup.select("ul > li > ul > li > a")]
    categories_url = ["http://books.toscrape.com/" + el["href"] for el in soup.select("ul > li > ul > li > a")]

    #little check before jump to getCategoryInfo.py module
    if len(categories_name) == len(categories_url):
        for i in range(len(categories_url)):
            getCategoryInfo.main(categories_url[i])
    else : 
        raise Exception ("Number of categories url not corresponding to numbre of categories")


if __name__ == "__main__":
    try:
        main("http://books.toscrape.com/index.html")
    except :
        print("Error : add a valid website url as an argument")