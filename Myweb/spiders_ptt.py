"""
當按下"已滿18歲"按鈕時，將傳遞該按鈕的value值(yes)，
並以post方法傳遞
"""

import requests
from bs4 import BeautifulSoup
"""
payload:建立post傳遞的參數，為字典型態，參數為from代表首頁網址及
yes代表驗證通過的資料yes
"""
payload={
    "from":"https://www.ptt.cc/bbs/Gossiping/index.html",  #請求的網址
    "yes":"yes" #按下的按鈕
    }

"""
headers:以user-agent使程式模擬瀏覽器，以騙過網站伺服器驗證(騙網站這是瀏覽器
"""
headers={
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)\
        AppleWebkit/537.36(KHTML, like Gecko)\
            Chrome/105.0.5195.127 Safari/537.36"    
    }
    
rs=requests.Session() #建立session物件

"""
使用session物件，以post方法項驗證頁面進行請求，此時會產生所屬的cookie,
以data參數設定傳遞的參數
以headers設定以撰寫的headers內容
"""
rs.post("https://www.ptt.cc/ask/over18",data=payload,headers=headers)
res=rs.get("https://www.ptt.cc/bbs/Gossiping/index.html",headers=headers)

soup=BeautifulSoup(res.text,"html.parser")
items=soup.select(".r-ent")
for item in items:
    print(item.select(".date")[0].text,item.select(".author")[0].text,\
          item.select(".title")[0].text)

