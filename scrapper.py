from importlib.metadata import requires
import requests


url = "https://www.booking.com/hotel/pl/happy-tower.html"
r = requests.get(url)

if r.status_code == 200:
    print('[INFO]: Roger.')
    print(r.text)
else:
    print(f"[INFO]: Something went wrong...\nStatus code: {r.status_code}")