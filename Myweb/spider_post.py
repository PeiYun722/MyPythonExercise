"""
requests.get及resquests.post差別(post網址列看不到附加的參數
"""
import requests
payload={"key1":"value1","key2":"value2"}
html=requests.post("http://httpbin.org/post",data=payload)
print(html.text)