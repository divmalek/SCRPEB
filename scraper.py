import requests
from bs4 import BeautifulSoup
import csv
print("Welcome to my code! This Python script scrapes eBay listings based on a provided URL. It extracts product information such as name, condition, price, location, shipping cost, and link. The data is then saved in a CSV file named 'ebay.csv'. It offers a convenient way to gather valuable information from eBay listings for analysis or research purposes.")
page = input("Entre The URL Of Page (ebay) > ")
page_url = requests.get(page).text
soup = BeautifulSoup(page_url,'lxml')
cards = soup.find_all("li",class_="s-item s-item__pl-on-bottom")
products = []

def main():
    for card in cards:
        product_name = card.find("div",class_="s-item__title").text.strip()
        condition = card.find("div",class_="s-item__subtitle").text.strip()
        shipping_cost_element = card.find("span", class_="s-item__shipping s-item__logisticsCost")
        if shipping_cost_element:
            shipping_cost = shipping_cost_element.text.strip()
        else:
            shipping_cost = "Shipping cost not found"
        price = card.find("div",class_="s-item__detail s-item__detail--primary").text.strip()
        location_element = card.find("span", class_="s-item__location s-item__itemLocation")
        if location_element:
            location = location_element.text.strip()
        else:
            location = "Location not found" 
        link = card.find("a",class_="s-item__link").get("href").strip()
        
        products.append({"Product Name":product_name,
                        "Product condition":condition,
                        "price":price,
                        "Product Location":location,
                        "Shipping Cost":shipping_cost,
                        "Product Link":link ,                   
                        })
    keys = products[0].keys()
        
    with open("ebay.csv","w",newline="",encoding="UTF-8") as f:
        writer = csv.DictWriter(f,keys)
        writer.writeheader()
        writer.writerows(products)
    print("File Created")
main()
