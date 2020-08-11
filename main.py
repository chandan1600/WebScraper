import bs4
import requests
import lxml

res = requests.get('http://books.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

