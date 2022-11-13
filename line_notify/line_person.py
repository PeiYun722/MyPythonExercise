import requests

def notify(msg,token):
    url="https://notify-api.line.me/api/notify"
    headers={"Authorization":"Bearer "+token}
    payload={"message":message}
    requests.post(url,headers=headers,params=payload)
    
token="2UQS2eARWpDaJ0A84VYpGu6PUbwyPac0uzMYzmw75Xw"
message="哈樓你好!!!"

notify(message,token)
    