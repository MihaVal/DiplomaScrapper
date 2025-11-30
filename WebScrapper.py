#Start of web scrapper diploma

from bs4 import BeautifulSoup
import requests

scrapped_page = requests.get("https://www.24ur.com/sport/odbojka/pajenk-radnicki-bo-naredil-vse-da-nam-zagreni-zivljenje.html")
soup = BeautifulSoup(scrapped_page.text, "html.parser")

quotes = soup.find_all("div", attrs={"class" : "comment__content"})
author = soup.find_all("a", attrs={"class" : "comment__author"})

for quote, author in zip (quotes, author):
    print(author.text + " - " + quote.text)
