"""
延續1，列出各電影的期待度及電影摘要
"""
import requests
from bs4 import BeautifulSoup
url="https://movies.yahoo.com.tw/movie_thisweek.html"
mhtml=requests.get(url)
soup = BeautifulSoup(mhtml.text,"lxml")
items=soup.find_all("div","release_info")
count=0
for item in items:
    cname=item.find("div","release_movie_name").a.text.strip()
    exp=item.find("div","leveltext").span.text.strip()
    txt=item.find("div","release_text").span.text.strip()
    count+=1
    print("電影編號:",count)
    print("中文名稱:",cname) 
    print("期待度:",exp)
    print("電影摘要:",txt)
    print()
