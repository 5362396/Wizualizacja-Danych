# Ze strony https://boardgamegeek.com pobierz linki (znajdź odpowiednie atrybuty) z sekcji 'Announcements'. Wyświetl te linki.
from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)
xpath = '//*[@class="media-module__body relative"]/div//h2//span//a//@href'
foundElements = page.xpath(xpath)
print(foundElements)