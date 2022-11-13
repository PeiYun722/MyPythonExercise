
"""
實作4:開眼電影望台北周末票房排行榜
"""
import requests
from bs4 import BeautifulSoup
url="http://app2.atmovies.com.tw/boxoffice/"
htmlfile=requests.get(url)
soup=BeautifulSoup(htmlfile.text,"lxml")
all=[]

trs=soup.find("table").find_all("tr") 
for tr in trs:
    movies=[]
    tds=tr.find_all("td")
    for td in tds:
        movies.append(td.text.strip())
    if movies and movies[0] !="more":
        all.append(movies)


print(all)
