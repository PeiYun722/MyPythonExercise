import requests
url="https://www.csf.org.tw/main/index.asp"
headers={
    "user-agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64)\
        AppleWebkit/537.36(KHTML, like Gecko)\
            Chorme/106.0.5249.103 Safari/537.36"
            }
    #user-agent業界公定寫法
r=requests.get(url,headers=headers)
print(r)