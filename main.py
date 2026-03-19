from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", action="store_true", help="List all game titles")
args = parser.parse_args()


url = "https://store.steampowered.com/search?maxprice=free&supportedlang=english&specials=1&ndl=1"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")


games = soup.find_all("span", class_="title")

print(f"Amount: {len(games)}")

if args.list:
    print("----------")
    for game in games:
        print(game.string)

