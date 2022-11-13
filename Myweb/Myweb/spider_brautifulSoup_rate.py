import requests
from bs4 import BeautifulSoup

url="http://taiwanrate.com/"
htmlfile=requests.get(url)
htmlfile.encoding="utf8"
soup=BeautifulSoup(htmlfile.text,"lxml")

ratetable=soup.find_all("table")
lefttop=ratetable[4].find("tr").find("tr").find("td")#銀行標題
print(lefttop.text,end="")
ratetop=ratetable[4].find("tr").find_all("a",class_="bodytablehead")
for head in ratetop:
    print(head.text,end="")
ratetd=ratetable[4].find("tr",class_="bodytabletr1")
print(ratetd.text)
while ratetd.find_next_sibling("tr"):
    ratetd=ratetd.find_next_sibling("tr")
    print(ratetd.text)
