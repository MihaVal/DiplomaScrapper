#Start of web scrapper diploma

from bs4 import BeautifulSoup
import requests

scrapped_page = requests.get("https://www.24ur.com/sport/odbojka/pajenk-radnicki-bo-naredil-vse-da-nam-zagreni-zivljenje.html")
soup = BeautifulSoup(scrapped_page.text, "html.parser")

#quotes = soup.find_all("div", attrs={"class" : "comment__content"})
#author = soup.find_all("a", attrs={"class" : "comment__author"})

#for quote, author in zip (quotes, author):
#    print(author.text + " - " + quote.text)

comment_block = soup.find_all("div", attrs={"class" : "comment"})

for comment in comment_block:
    author_part = comment.find("a", attrs={"class" : "comment__author"})
    text_part = comment.find("div", attrs={"class" : "comment__content--body"})
    rating_part = comment.find("a", attrs={"class" : "comment__vote"})

    """
    dodajaj stvari ki jih hočeš vidit drugo pa izpusti in se ne bi smelo 
    pokazat na konc (npr tisti icons stuff) težava ki me bega trenutno
    je da bi rad vseeno dobil podatek lajkov in dislajkov, brez tistega
    icons stuffa zraven ali pa da bi to preimenoval da bi bilo jasno 
    zakaj se gre(npr kaj je ta podatek) nekaj stvari pa tudi izpustil 
    sigurno (vprašanje tudi a je pomemben podatek je koliko komentov je
    v subthreadu drugih komentov ki pokaže engagement level glede 
    na polarnost komentarja posameznega recimo)
    """
    author = author_part.get_text(strip=True) if author_part else ""
    text = text_part.get_text(" ", strip=True) if text_part else ""
    rating = rating_part.get_text(strip=True) if rating_part else ""

    print(f"{author}: {text} | {rating}")