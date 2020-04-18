from bs4 import BeautifulSoup
from selenium import webdriver
import json

driver = webdriver.Firefox()
driver.get("https://www.walgreens.com/q/toilet+paper")

html = driver.page_source
content = BeautifulSoup(html, "html.parser")

data = []
for tp_data in content.find_all("div", attrs={"class": "wag-product-card-details wag-product-card-width_b"}):
    tp_object = {
        "price": tp_data.find("span", attrs={"class": "product__price"}).text,
        "availability": tp_data.find("p", attrs={"class": "wag-channal-availabilitytxt"}).text
    }
    data.append(tp_object)

with open ("toilet_paper_data.json", "w") as outfile:
    json.dump(data, outfile)
driver.quit()