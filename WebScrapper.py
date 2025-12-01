#Start of web scrapper diploma

from bs4 import BeautifulSoup
import requests

scrapped_page = requests.get("https://www.24ur.com/articles/4482768/comments/from_comment_id/01KBDS85J4PZDY5C00AZGGWQEE")
soup = BeautifulSoup(scrapped_page.text, "html.parser")

#quotes = soup.find_all("div", attrs={"class" : "comment__content"})
#author = soup.find_all("a", attrs={"class" : "comment__author"})

#for quote, author in zip (quotes, author):
#    print(author.text + " - " + quote.text)

comment_block = soup.find_all("div", attrs={"class" : "comment"})

for comment in comment_block:
    author_part = comment.find("a", attrs={"class" : "comment__author"})
    text_part = comment.find("div", attrs={"class" : "comment__content--body"})
    likes = comment.find("span", attrs={"class" : "comment-likes-positive"})
    dislikes = comment.find("span", attrs={"class" : "comment-likes-negative"})
    print("Total comments scraped:", len(comment_block))    
    """
    250 komentarjev, like 200 jih manka??
    """
    author = author_part.get_text(strip=True) if author_part else ""
    text = text_part.get_text(" ", strip=True) if text_part else ""
    rating_plus = likes.get_text(strip=True) if likes else ""
    rating_minus = dislikes.get_text(strip=True) if dislikes else ""
    
    print(f"{author}: {text} | Všečki/Nevšečki [+{rating_plus}/-{rating_minus}]")

    
