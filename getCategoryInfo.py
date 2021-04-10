#TODO : Shebang 

import argparse
import requests
import getBookInfo
from bs4 import BeautifulSoup


def getBooksUrlOnAPage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    array_of_a = soup.select("h3 > a")
    array_books_url = []
    for el in array_of_a:
        array_books_url.append(el["href"].replace("../../..", "http://books.toscrape.com/catalogue"))
    return array_books_url


def getPagesUrl(base_url, num_page):
    array_page_url = []
    for num in range(num_page):
        if num == 0:
            array_page_url.append(base_url)
        else:
            
            array_page_url.append(base_url.replace('index', 'page-'+ str(num+1) ))
    return array_page_url


def main(array_category_url):
    for category_utl in array_category_url:
        response = requests.get(category_utl)
        if response.ok:
            soup = BeautifulSoup(response.content, "html.parser")

            #get the number of book on this category 
            book_number = int(soup.find("form", {"class":"form-horizontal"}).find("strong").text)

            # get the number of pages
            if book_number > 20 : 
                page_number = int(soup.find("li", {"class":"current"}).text.strip()[-1])
            else :
                page_number = 1

            # get an array of the pages urls 
            array_page_url = getPagesUrl(category_utl, page_number)

            # get all books urls of this category
            array_books_url = []
            for el in array_page_url:
                page_book_list = getBooksUrlOnAPage(el)
                array_books_url.extend(page_book_list)


        if len(array_books_url) == book_number:
            getBookInfo.main(array_books_url)


   
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Enter a valid category url")
    args = parser.parse_args()

    try:
        array_category_url = [args.url]
        main(array_category_url)
    except :
        print("Error : add a valid categorie_page_url as an argument")


# http://books.toscrape.com/catalogue/category/books/sequential-art_5/page_2.html

# http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
# print(len(array_books_url))