import requests
from fake_useragent import UserAgent
ua=UserAgent()
headers={"user-agent":ua.random}
url="https://www.momoshop.com.tw/main/Main.jsp"
r=requests.get(url,headers=headers)
print(r.status_code)#200:成功
print(r.text)

"""""""""
if (r=requests.get(url))--->出現錯誤
    because有防爬機制，網站偵測到不為瀏覽器，故拒絕連線
"""""""""