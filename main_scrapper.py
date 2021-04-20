#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program is the main entry to scrape https://books.toscrape.com/
    See README for more details

    This program while output .csv file and .jpg files in './exports/' folder"""

import argparse
from scrapper_books_toscrape import getAllCategoryInfo, getCategoryInfo, getBookInfo

# all
# https://books.toscrape.com/ 

# Categorie
# https://books.toscrape.com/catalogue/category/books/travel_2/index.html

# Book
# https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html

def main(url):
    """This function analyze the url, and send it to the right module
    Args:
        url (str): url of the website or a category or a book
    """
    update_url = url.replace('https://books.toscrape.com/', '')
    if update_url == '':
        try:
            getAllCategoryInfo.main(url)
        except:
            print("ERROR : URL Not Found")
            
    elif "category" in update_url:
        try:
            getCategoryInfo.main(url)
        except:
            print("ERROR : URL Not Found")
    else:
        try :
            getBookInfo.main([url])
        except :
            print("ERROR : URL Not Found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help='url to scrape')

    args = parser.parse_args()
    main(args.url)