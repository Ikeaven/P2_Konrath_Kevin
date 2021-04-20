#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
    This module collects Book's informations from books_toscrap website.
    All data, once collected, are writen in a .csv file, in "exports" folder.  
"""


import requests
import csv
import argparse
import os 
import sys
import re

from bs4 import BeautifulSoup
from progress.bar import Bar
# from utility.decorators import timer


def extract_number(str):
    """Return all numeric characters of a string as an int
    params :
        str (str) : string that contains numeric characters
    return :
        (int) : join of all integers in str
    """ 
    num_list = []
    for el in str:
        if ord(el)>= 48 and ord(el)<=57:
            num_list.append(el)
    return int(''.join(num_list))


def convert_ratingString_in_number(str):
    """Return the conversion in integer or an error message
    params :
        str (str) : string who represebts a number between One to Five
    return :
        (int) : corresponding to the string params"""
    num_table = ['One', 'Two', 'Three', 'Four', 'Five']
    if str in num_table: 
        for i, el in enumerate(num_table):
            if str == el:
                return i+1 
    else :
        raise ValueError ('Function convert_ratingString_in_number() need a string parameter who represent a numbre between One to Five')


def download_image(image_url, category_name):
    """Download a picture and create folders to store the picure in the right category folder
    params : 
        image_url : string - picture's url 
        category_name : string - used to create folder for this category
    output : 
        picture file in category's folder
    """
    response = requests.get(image_url)

    # Set image_name with image_url
    image_name = image_url.replace('http://books.toscrape.com/media/cache/', '').replace('/','_')

    #check if .exports/images folder exists
    if os.path.isdir("./exports/images")==False:
        os.mkdir("./exports/images")

    #check if .exports/images/[category_name] folder exists
    if os.path.isdir("./exports/images/"+category_name) == False:
        os.mkdir("./exports/images/"+category_name)

    open("./exports/images/"+category_name+"/"+ image_name, 'wb').write(response.content)


# @timer
def extract_book_data(product_page_url):
    """This function extract data from book's url.
    Args:
        product_page_url (str): book's url.
    Returns:
        upc (str) : upc code. 
        title (str) : book's title
        price_including_tax (str) : price with devise symbol
        price_excluding_tax (str) : price with devise symbol 
        number_available (int) : number 
        product_description (str) : book's description 
        category (str) : book's category
        review_rating (int) : rating  
        image_url (str) :  string, image's url
    """
    # get request with user agent 
    # headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
    # response = requests.get(product_page_url, headers=headers)
    # ---------------
    response = requests.get(product_page_url)
            
    #Returns True if status_code is less than 400, False if not.
    if response.ok: 
        soup = BeautifulSoup(response.content, "lxml")
        
        # Récupration du tableau en entier puis extraction : 1 seul analyse du DOM
        tr = soup.find_all("tr")
        upc = tr[0].find('td').text
        price_including_tax = tr[3].find('td').text
        price_excluding_tax = tr[2].find('td').text
        number_available = extract_number(tr[5].find('td').text)
        # ----- FIN Récupération des données du tableau en entier

        # Récuperation des données du tableau avec plusieurs analyse de DOM. 
        # upc = soup.select_one('tr > td').string
        # price_including_tax = soup.select_one('tr:nth-child(4) > td').string
        # price_excluding_tax = soup.select_one('tr:nth-child(3) > td').string                
        # number_available = extract_number(soup.select_one('tr:nth-child(6) > td').string)
        # ------- FIN Récuperation des données du tableau avec plusieurs analyse de DOM. ----

        title = soup.find('h1').text.replace(',', '')

        if soup.select("#product_description") == []:
            product_description = ""
        else :
            product_description = soup.select_one('article > p').string

        category = soup.find("ul").select_one('li:nth-child(3)>a').string.strip()
        review_rating = convert_ratingString_in_number(soup.select_one('.star-rating').attrs['class'][1])
        image_url = soup.select_one('.carousel-inner>div>img')["src"].replace('../../', 'http://books.toscrape.com/')

        return (upc, title, price_including_tax,
                price_excluding_tax, number_available, product_description, 
                category, review_rating, image_url)
    else:
        response.raise_for_status()   


def main(url_list, category_name='No_category'):
    """Collect book's data than create a .csv in './exports/[Subfolder]/', 
    Then download book's picture, and store it in ./exports/images/[Subfolder]/'.
    Subfolder's name follow category_name. 
    
    params : 
        url_list (array) : list of book's url 
        category_name : category associated to the list
    outputs : 
        .csv files in ./exports/[Subfolder]/ 
        .jpg files in ./exports/images/[Subfolder]/

    """
    # For only one book, replace category_name by book's name 
    if category_name == 'No_category' :
        category_name = url_list[0].replace('https://books.toscrape.com/catalogue/', '').replace('/index.html', '').replace('_','')
        category_name = re.sub(r'[0-9]+', '', category_name)

    # create exports folder if necessary 
    if os.path.isdir("./exports") == False:
        os.mkdir("./exports")   

    with open( './exports/'+category_name+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')

        # write header row                    
        spamwriter.writerow(["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
        "number_available", "product_description", "category", "review_rating", "image_url"])

        with Bar('Processing', max=len(url_list)) as bar:
            for product_page_url in url_list:

                #récupération des donnés de livre
                (upc, title, price_including_tax, 
                price_excluding_tax, number_available, product_description, 
                category, review_rating, image_url) = extract_book_data(product_page_url)
                download_image(image_url, category_name)
                
                #write row with books data 
                spamwriter.writerow([
                    product_page_url,
                    upc, 
                    title, 
                    price_including_tax, 
                    price_excluding_tax, 
                    number_available, 
                    product_description, 
                    category, 
                    review_rating, 
                    image_url
                    ])   

                bar.next()
            print("")
            print("______________________________________________")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="book url")
    parser.add_argument("category_name", help="name of a category, it's used for the output file's name")
    args = parser.parse_args()

    try:
        arrayUrl = [args.url]
        main(arrayUrl, args.category_name)
    except :
        print("Error : add a valid book_page_url as an argument" +  sys.exc_info())

