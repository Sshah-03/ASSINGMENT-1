import requests
import bs4
res = requests.get("http://127.0.0.1:5500/MilestoneUI/Tic_Tac_Toe.html")
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)
