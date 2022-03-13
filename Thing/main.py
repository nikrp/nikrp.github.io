# Imports
from bs4 import BeautifulSoup
import requests
import os

# Change the directory to ./Thing
os.chdir("./Thing")

# Request the code from the website
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
empireMovieTxt = response.text

# Create my soup
soup = BeautifulSoup(empireMovieTxt, "html.parser")

# Get all the tags where the titles reside
imgAlt = soup.find_all(name="img", class_="jsx-952983560 loading")
imgAltList = []

# Get all the titles into a list
for tag in imgAlt:
    alt = tag.get("alt")
    imgAltList.append(alt)

# Count settings
count = soup.find_all(name="span", class_="jsx-4245974604 listicle-item-count")
newCount = []
for place in count:
    countList = place.getText().split(" of ")
    newCount.append(countList[0])

# Make and fill the dictionary with rank and title as key and value
movieNumNameDict = {}
for num in newCount:
    movieNumNameDict[num] = imgAltList[newCount.index(num)]

# Add everything to file
file = open("movies.txt", "w", encoding="utf8")
for (key, value) in movieNumNameDict.items():
    name = f"{key}) {value}"
    print(name)
    file.write(f"{name}\n")
file.close()