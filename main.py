import bs4
import requests
import lxml

res = requests.get('http://books.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

productName = []
productPrice = []

for altText in soup.find_all('img', src=True):
    productName.append(altText['alt'])
    print(productName[-1])

for price in soup.find_all('p', {'class':'price_color'}):
    productPrice.append(price.text)
    print(productPrice[-1])