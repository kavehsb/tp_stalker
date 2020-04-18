from bs4 import BeautifulSoup
import requests
import json

url = "https://www.walgreens.com/q/toilet+paper"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

data = []
for tp_data in content.find_all("div", attrs={"class": "wag-product-card-details wag-product-card-width_b"}):
    unwanted = content.find_all("span", attrs={"class": "sr-only"})
    for span in unwanted:
        span.extract()
    tp_object = {
        "price": tp_data.find("span", attrs={"class": "product__price"}).text.strip(),
        "availability": tp_data.find("p", attrs={"class": "wag-channal-availabilitytxt"}).text.strip()
    }
    data.append(tp_object)

with open ("toilet_paper_data.json", "w") as outfile:
    json.dump(data, outfile)