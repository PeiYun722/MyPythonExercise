"""""""""
讀取ex_3.html，並將國家及河川放入dict
"""""""""
import requests
from bs4 import BeautifulSoup

url=r"C:\Mypython\Myweb\ex_3.html"
htmlfile=open(url,encoding="utf8")

objsoup=BeautifulSoup(htmlfile,"lxml")

tableobj=objsoup.find("table").find("tbody")
tables=tableobj.find_all("tr")

myriver=[]
for table in tables:
    river=table.find("td")
    myriver.append(river.text)
    
print(myriver)
mycountry=[]
for table in  tables:
    countries=table.find_all("td")
    country=countries[1]
    mycountry.append(country.text)
    
print("國家:",mycountry)
print("河川:",myriver)
print("-"*20)
data=dict(zip(mycountry,myriver))
print(data)