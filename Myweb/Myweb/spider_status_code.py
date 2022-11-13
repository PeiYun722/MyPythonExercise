import requests
url="https://www.utaipei.edu.tw"
htmlfile=requests.get(url)
            #status_code:狀態碼
if htmlfile.status_code==requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容的大小=",len(htmlfile.text))
else:
    print("取得網頁內容失敗")