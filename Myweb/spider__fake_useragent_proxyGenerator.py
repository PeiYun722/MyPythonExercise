import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
ua=UserAgent()
url="https://free-proxy-list.net/"

def proxyGenerator():
    headers = {"user-agent":ua.random}
    htmlfile=requests.get(url,headers=headers)
    soup=BeautifulSoup(htmlfile.text,"lxml")
    proxies_table=soup.find("table",class_="table table-striped table-bordered")
    proxies=[]
    for row in proxies_table.tbody.find_all("tr"):
        proxies.append({
            "http":"http://"+row.find_all("td")[0].text + ":" +
                row.find_all("td")[1].string,
            "https":"https://"+row.find_all("td")[0].text + ":" +
                row.find_all("td")[1].string,
        })
    return random.choice(proxies) 
    
"""
主程式
"""
for n in range(5):
    proxy=proxyGenerator()
    print(proxy)