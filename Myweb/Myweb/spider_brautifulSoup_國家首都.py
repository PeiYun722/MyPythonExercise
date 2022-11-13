"""""""""
讀取ex_2.html，並將國家及首都加成dict
"""""""""
import requests
from bs4 import BeautifulSoup
url=r"C:\Mypython\Myweb\ex_2.html"
file=open(url,encoding='utf-8')
print(file)
sp=BeautifulSoup(file,"lxml")
print(sp.prettify())

mycity=[]
cityobj=sp.find("dl")
cities=cityobj.find_all("dt")#返回所有dt
for city in cities:
    mycity.append(city.text)

mycountry=[]
countryobj=sp.find("dl")
countries=countryobj.find_all("dd")
for country in countries:
    mycountry.append(country.text)
    
print("國家:",mycountry)
print("首都:",mycity)
print("-"*20)

#將mycountry及mycity一對一加入到dict裡
data=dict(zip(mycountry,mycity))
print(data)

"""""""""
<dt>通常表示項目的標題，而<dd>則為項目的敘述，會自動縮排
<dt>及<dd>皆在<dl>裡
"""""""""


