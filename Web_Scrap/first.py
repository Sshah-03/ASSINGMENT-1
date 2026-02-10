import requests
result = requests.get("http://example.com/")
print(type(result))

print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
 
print(soup.select("title"))
# To get just text use:
print(soup.select("title")[0].getText())

soup1 = soup.select("p")[0]
print(soup1)
print(type(soup1))