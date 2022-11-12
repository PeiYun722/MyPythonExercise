from bs4 import BeautifulSoup

#設定html原始碼變數，html要以"註解"方式建立
html="""
<html>
    <head><meta charset="utf-8"><title>這是網頁標題</title></head>
    <body>
        <p id="p1">這是段落一</p>
        <p id="p2" class ="red">這是段落二</p>
    </body>
</html>
"""

sp=BeautifulSoup(html,"html.parser") #html.parser:解析方法
print(sp.find("p")) #找第一筆
print(sp.find_all("p")) #找全部資料，以串列方式回傳

"""
尋找第一個<p>標籤，條件為id="p2",class_="red"
"""
print(sp.find("p",{"id":"p2","class":"red"})) #字典格式
print(sp.find("p",id="p2",class_="red"))

print(sp.prettify())