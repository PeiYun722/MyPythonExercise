"""
判斷網址讀取狀態
"""
import requests
url="https://www.csf.org.tw/main/index.asp"
r=requests.get(url)
r.encoding="utf-8"

#檢查回應碼是不是200
if r.status_code == requests.codes.ok:
    print(r.text)

"""
HTTP狀態碼(表達一個HTTP請求是否被完成):
    1.Informational respones (資訊回應):100~199
    2.Successful responses (成功回應):200~299 (200
    3.Redrects (重新導向):300~399 
    4.Client error (用戶端錯誤):400~499 (404
    5.Server error (伺服器端錯誤):500~599 (500:Internal Sever error
"""