"""""""""
讀取ex_1.html，並列印出台灣最健康大學排名資料
"""""""""
import requests
from bs4 import BeautifulSoup

url=r"C:\Mypython\Myweb\ex_1.html"
htmlfile=open(url,encoding="utf8")

#objSoup:所有網頁內容結構
#lxml解析方法比html.parser新(快一點
objSoup=BeautifulSoup(htmlfile,"lxml")


#titleobj:從objsoup取出所有的<h2>標籤(儲存為串列)
titleobj=objSoup.find_all("h2")
print(titleobj[2].text)#列印第三個串列內容

"""
itemobj:尋照itemobj中的<ol>標籤且屬性為type="I"，
        傳回第一個找到的項目(即<ol type="I">)
"""
itemobj=objSoup.find("ol",type="I")
print("這:",itemobj,"好")

"""
items:尋找itemobj中所有的<li>標籤，
      即(<ol type="I">範圍內的所有<li>，
      以迴圈將items中的所有內容印出
"""
items=itemobj.find_all("li")
for item in items:
    print(item.text)
    
print(itemobj)

"""""""""
<ol>:序號列表(項目編號)，每一項編號皆為一個<li>，
     編號樣式由<ol type="樣式"指定>
<ul>:無序號列表
"""""""""


