from bs4 import BeautifulSoup
import requests
import json


# Sifts through html on walgreens and stores information about
#   item, price, and availability in a list of dicts
#   to be returned and stored in a database
def get_data():
    url = "https://www.walgreens.com/q/toilet+paper?N=1336"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    
    data = []
    for tp_data in content.find_all("div", attrs={"class": "wag-product-card-details wag-product-card-width_b"}):

        # Remove unwanted nested elements
        unwanted = content.find_all("span", attrs={"class": "sr-only"})
        for span in unwanted:
            span.extract()

        item = tp_data.find("a", attrs={"name": "product-title"}).text.strip()
        price = tp_data.find("span", attrs={"class": "product__price"}).text.strip()
        availability = tp_data.find("p", attrs={"class": "wag-channal-availabilitytxt"}).text.strip()

        if price == "":
            price = "Price available in store"

        tp_object = {
            "item": item,
            "price": price,
            "availability": availability,
        }
        data.append(tp_object)
    return data
