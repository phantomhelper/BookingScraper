from importlib.metadata import requires
from itertools import count
from bs4 import BeautifulSoup
import requests


url = "https://www.booking.com/hotel/pl/happy-tower.html#tab-reviews"
#url = "https://www.booking.com/hotel/pl/happy-tower.html"

r = requests.get(url)

if r.status_code == 200:
    print('[INFO]: Roger.')

    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)
    reviews = soup.select("li.review_list_new_item_block")
    print(len(reviews))


else:
    print(f"[INFO]: Something went wrong...\nStatus code: {r.status_code}")