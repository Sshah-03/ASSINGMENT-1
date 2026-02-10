import requests
import bs4
res = requests.get('https://quotes.toscrape.com/')
#print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(soup.select('.author')) 
#print(soup)
authors = set()
#for name in soup.select('.author'):
 #   authors.add(name.text)
#print(authors)
#print(soup.select('.text'))
#quotes = []
#for quotes in soup.select('.text'):
 #   quotes.append(quotes.text)
#print('\n',quotes)

#print(len(soup.select('.tag-item')))
#for item in soup.select('.tag-item'):
 #   print(item.text)

url = 'http://quotes.toscrape.com/page/'
authors = set()
for page in range(1,10):
    page_url = url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
print(authors)
     
