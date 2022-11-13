import requests
from bs4 import BeautifulSoup

url="http://ehappy.tw/bsdemo1.htm"
html=requests.get(url)
html.encoding="utf-8"

"""
sp:建立BeautifulSoup物件，帶入html，解析方法html.parser
BeautifulSoup(原始碼,解析方法)
"""
sp=BeautifulSoup(html.text,"html.parser")

print(sp.title) #取得整個<title>標籤
print(sp.title.text) #取得<title>標籤作用內容
print(sp.h1)
print(sp.p)

