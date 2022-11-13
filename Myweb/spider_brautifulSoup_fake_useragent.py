"""
實作5:博客來全館及時排行綁存入CSV
"""
import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent

url="https://www.books.com.tw/web/sys_hourstop/home?loc=P_0007_001"
csvfile=r"C:\MyPython\Myweb\books1.csv"
ua=UserAgent()
headers={"user-agent":ua.random}
htmlfile=requests.get(url,headers=headers)
soup=BeautifulSoup(htmlfile.text,"lxml")

tag_ul=soup.find("ul",class_="clearfix")
rows=tag_ul.find_all("li",class_="item")
print(len(rows))
items=[]

for row in rows:
    item=[]
    top=row.find("strong",class_="no").text.strip()
    item.append(top)
    title=row.find("h4")#名稱
    item.append(title.text.strip())
    item.append(title.find("a").get("href"))#網址:<h4>下的<a>.href值
    img=row.find("img",class_="cover")
    item.append(img.get("src"))#圖片:<img>,class:cover,src值
    price=row.find("ul",class_="msg").find("li",class_="price_a")
    item.append(price.text.strip())#優惠價:<ul>,class:msg下<li>,class:price_a
    items.append(item)
    
"""""""""
寫入CSV
"""""""""
with open (csvfile,"w+",newline="",encoding="utf-8-sig")as fp:
    writer=csv.writer(fp)
    writer.writerow(["排名","名稱","網址","圖片","價格"])
    for item in items:
        writer.writerow(item)
        
"""""""""
CSV亂碼問題:
    系統(尤其是windows)在產生文字檔時(此通常為預設)
    通常在檔案開始處會加入BOM(ByteOrder Mark;位元組序標示)
    功用為辨識為哪種格式的檔案(用於Unicode編碼)
  utf-8:以位元組為編碼方式，其位元組序在所有系統皆相同，故無需加入BOM，
        若讀取帶有BOM的utf-8檔案時，會將BOM檔做檔案內容，故顯示亂碼
  utf-8-sig:signature，帶有BOM的utf-8，會將BOM個別取出處理，隔離原文
        文字內容，故不會有亂碼產生
"""""""""
    
    