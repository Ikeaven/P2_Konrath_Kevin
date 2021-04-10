#! ./env/bin/python
# coding: utf-8 

import requests
import csv
import argparse

from bs4 import BeautifulSoup

# product_page_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

parser = argparse.ArgumentParser()
parser.add_argument("url", help="book url")
args = parser.parse_args()



def extract_number(str):
    """Return all numeric characters of a string as an int""" 
    num_list = []
    for el in str:
        if ord(el)>= 48 and ord(el)<=57:
            num_list.append(el)
    return int(''.join(num_list))

def convert_ratingString_in_number(str):
    """Return the conversion in integer or an error message"""
    num_table = ['One', 'Two', 'Three', 'Four', 'Five']
    num = 6
    for i, el in enumerate(num_table):
        if str == el:
            return i+1 
   
def main(url, nb_book=1):
    """Create a .csv containing the info of the book."""
    product_page_url = url
    response = requests.get(product_page_url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        tr = soup.findAll("tr")

        upc = tr[0].find('td').text
        price_including_tax = tr[3].find('td').text
        price_excluding_tax = tr[2].find('td').text
        number_available = extract_number(tr[5].find('td').text)
        title = soup.find('h1').text.replace(',', '')
        product_description = soup.find('article').findAll('p')[-1].text.replace(',', '')
        category = soup.find("ul").findAll("li")[2].text.strip()
        review_rating = convert_ratingString_in_number(soup.findAll("p")[2]["class"][1])
        image_url = soup.find('img')["src"]
        



    with open('book_info.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        if nb_book == 1:                        
            spamwriter.writerow(["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax",
            "number_available", "product_description", "category", "review_rating", "image_url"])

        spamwriter.writerow([product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, 
        review_rating, image_url])   

  
if __name__ == "__main__":
    try:
        main(args.url)
    except :
        print("Error : add a valid book_page_url as an argument")

