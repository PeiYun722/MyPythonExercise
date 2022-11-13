"""
實作3:Yahoo電影票房排行榜資料並存入CSV檔
"""
import requests
from bs4 import BeautifulSoup
import csv
url="https://movies.yahoo.com.tw/chart.html"
csvfile="C:\MyPython\Myweb\yahoomovie.csv"
htmlfile=requests.get(url)
htmlfile.encoding="utf8"
soup = BeautifulSoup(htmlfile.text,"lxml")

rows=soup.find_all("div",class_="tr")#所有"div"下的<tr>(標格列)
#rows.pop(0):取出第一列，並以stripped.strings取出標題字串內容以建立標題列
colname=list(rows.pop(0).stripped_strings)
items=[]
for row in rows:
    tds=row.find_all("div",class_="td")
    item=[]
    item.append(tds[0].text)#tds:每一列中所有<div>下的<td>(表格欄)
    item.append(tds[2].text)
    title=tds[3].text.strip()
    
    #針對第一列(第一名)片名np.array([0])
    if "\n" in title:
        x=title.split("\n")#判斷是否為多行，如果是，則取第一行文字
        title=x[0]
        
    item.append(title)
    item.append(tds[4].text.strip())
    item.append(tds[5].text.strip())
    item.append(tds[6].text.strip())
    items.append(item)
"""
寫入csv
"""
with open(csvfile,"w+",newline="",encoding="utf8") as fp:
    writer=csv.writer(fp)
    writer.writerow(colname)
    for item in items:
        writer.writerow(item)