"""
查詢參數定義為字典資料，加入get請求中
"""
import requests
payload={"key1":"value1","key2":"value2"}
r=requests.get("http://httpbin.org/get",params=payload)#用params帶出查詢參數
print(r.text)#print 程式碼
print("---")
print(r.url)#print網址