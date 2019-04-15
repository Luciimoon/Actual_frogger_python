import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=legos&_sacat=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 's-item__title'}):
          href = "https://www.ebay.com" + link.get('href')
          title = link.string
          print(href)
          print(title)
        page += 1
def get_single_item_data(item_url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soupfindAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://www.ebay.com" + link.get('href')
        print(href)


trade_spider(3)