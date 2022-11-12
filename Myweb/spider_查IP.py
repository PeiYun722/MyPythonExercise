import requests
url="https://api.ipify.org"
r=requests.get(url)
print("我目前的IP是:",r.text)