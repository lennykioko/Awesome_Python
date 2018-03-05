import requests, csv
from bs4 import BeautifulSoup

business = "banks"
location = "kenya"
url = "http://www.yellowpageskenya.com/site/index?SearchForm%5Bwhat%5D={}&SearchForm%5Bwhere%5D={}".format(business, location)

r = requests.get(url)
content = r.content
soup = BeautifulSoup(content, "html.parser")

data_page = soup.find("li", {"class": "last"}).find("a", href=True)["data-page"]
data_page = int(data_page) + 1

for i in range(1, data_page):
    current_url = "http://www.yellowpageskenya.com/site/index?SearchForm%5Bwhat%5D={}&SearchForm%5Bwhere%5D={}&page={}&per-page=50".format(business, location, i)
    r = requests.get(current_url)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")

    blocks = soup.find_all("div", {"class": "listing__content"})

    for i in range(len(blocks)):
        name = blocks[i].find("a", {"class" : "listing__name--link jsListingName"}).text
        address = blocks[i].find("span", {"class" : "jsMapBubbleAddress"}).text
        website = blocks[i].find("a", {"class" : "mlr__item__cta"})
        phones = blocks[i].find_all("li", {"class" : "mlr__submenu__item"})

        if website is None:
            website_link = "We need a website"
        else:
            website_link = website["href"]


        if len(phones) == 1:
            phone = blocks[i].find("li", {"class" : "mlr__submenu__item"})
            phone_number = phone.text
        else:
            phone_number = []
            for i in range(len(phones)):
                phone_number.append(phones[i].text)
            phone_number = phone_number[0]
        
        with open("yellow_pages.csv", "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([name, address, website_link, phone_number])
