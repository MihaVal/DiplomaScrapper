#Start of web scrapper diploma

from bs4 import BeautifulSoup
import requests

scrapped_page = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(scrapped_page.text, "html.parser")

quotes = soup.find_all("span", attrs={"class" : "text"})
authors = soup.find_all("small", attrs={"class" : "author"})

for quote, author in zip (quotes, authors):
    print(quote.text + " - " + author.text)
