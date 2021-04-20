#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""""

import argparse
from scrapper_books_toscrape import getAllCategoryInfo, getCategoryInfo, getBookInfo

# all
# https://books.toscrape.com/ 

# Categorie
# https://books.toscrape.com/catalogue/category/books/travel_2/index.html

# Book
# https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html

def main(url):
    update_url = url.replace('https://books.toscrape.com/', '')
    if update_url == '':
        getAllCategoryInfo.main(url)
    elif "category" in update_url:
        getCategoryInfo.main(url)
    else:
        getBookInfo.main([url])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help='url to scrape')

    args = parser.parse_args()
    main(args.url)