import requests

# ==============================
#      Notify設定
# ==============================

def notify(msg, token):
    url = "https://notify-api.line.me/api/notify"         # Notify網址 
    headers = {"Authorization": "Bearer " + token}        # HTTPS表頭
    payload = {"message": message}                        # HTTPS內容
    requests.post(url, headers=headers, params=payload)   # 提出POST請求
    

# 發送訊息
token = "pfrc9Rga9g4TNOD1CeRToZpnbktPuie2k9p01wEuEkx"     # 你的token
message = "今天天氣真好！"
notify(message, token)
