from bs4 import BeautifulSoup
import requests
from os import chdir

chdir("./Thing")

""" with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

 """

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
ycWebpage = response.text

soup = BeautifulSoup(ycWebpage, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
articleTexts = []
articleLinks = []
for articleTag in articles:
    articleText = articleTag.getText()
    articleTexts.append(articleText)
    articleLink = articleTag.get("href")
    articleLinks.append(articleLink)
    
articleUpvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

maxUpvotesIndex = articleUpvotes.index(max(articleUpvotes))
articleLinks.remove(articleLinks[len(articleLinks) - 1])
print(articleTexts[maxUpvotesIndex])
print(articleLinks[maxUpvotesIndex])
print(articleUpvotes[maxUpvotesIndex])

# print(articleTexts)
# print("\n\n\n\n\n")
# print(articleUpvotes)
# print("\n\n\n\n\n")
# print(articleLinks)