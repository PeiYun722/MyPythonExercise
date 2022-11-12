"""
專題三:Yahoo電影
    (1)本週新片:
        本周新片網頁區間:<div class="release_info">
        中文片名:<div class="release_movie_name">
        英文片名:<div class="en">
        上映日期:
"""
import requests
from bs4 import BeautifulSoup
url="https://movies.yahoo.com.tw/movie_thisweek.html" 
mhtml=requests.get(url)
soup = BeautifulSoup(mhtml.text,"lxml")
movienum=0
items=soup.find_all("div","release_info")
for item in items:    
    chinese_title=item.find("div","release_movie_name").a.text.strip()
    english_title=item.find("div","en").a.text.strip()
    rtime=item.find("div","release_movie_time").text.strip()
    movienum+=1
    print("新片編號:",movienum)
    print("中文片名:", chinese_title)
    print("英文片名:",english_title)
    print(rtime)
    print()