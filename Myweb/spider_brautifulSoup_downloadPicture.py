"""
下載yahoo劇照，並存至電腦
"""

import requests
from bs4 import BeautifulSoup
import os
url="https://movies.yahoo.com.tw/movie_thisweek.html"
htmlfile=requests.get(url)

#soup:新片網頁的HTML
soup=BeautifulSoup(htmlfile.text,"lxml")
items=soup.find_all("div","release_foto")

#photos:存放劇照的串列
photos=[]

for item in items:
    photo=item.a.img["data-src"]#圖片的網址
    photos.append(photo)

desDir=r"C:\MyPython\Myweb\picture"#存放位置
if os.path.exists(desDir) == False: #如果檔案不存在
    os.mkdir(desDir)#創建資料夾
print("搜尋到的圖片數量=",len(photo))

for photo in photos:
    picture=requests.get(photo)#下載圖片
    """
    raise_for_status():增加requests.exceptions.HTTPError針對Client 4XX,
                5XX Error使用本程式用於驗證圖片下載是否成功
    """
    picture.raise_for_status()
    print("%s圖片下載成功"%photo)
    #os.path.basename():去除檔案路徑，傳回該檔案名稱(含副檔名)
    pictFile=open(os.path.join(desDir,os.path.basename(photo)),"wb")
    
    for diskStorge in picture.iter_content(10240):
        pictFile.write(diskStorge)
    pictFile.close()
    
"""
requests.get()如果容量很大，可加參數steam=True
"""