import requests
from bs4 import BeautifulSoup
import csv
csvfile=r"C:\MyPython\Myweb\twrate.csv"
url="http://taiwanrate.com/"

tablelist=[] #總表
ratelist=[] #利率
headlist=[] #總標頭

htmlfile=requests.get(url)
htmlfile.encoding="utf8"
soup=BeautifulSoup(htmlfile.text,"lxml")

ratetable=soup.find_all("table")
lefttop=ratetable[4].find("tr").find("tr").find("td") #"銀行"
headlist.append(lefttop.text) #將"銀行"加入標頭
ratetop=ratetable[4].find("tr").find_all("a",class_="bodytablehead")#所有利率標頭
for head in ratetop:
    headlist.append(head.text) #將所有利率標頭加入總標頭
    
tablelist.append(headlist) #將總標頭加入到總表
ratetd=ratetable[4].find("tr",class_="bodytabletr1")
for row in ratetd:
    ratelist.append(row.text)#將第一列所有<td>下文字放入ratelist
tablelist.append(ratelist)#將第一列利率資料放入總表

while ratetd.find_next_sibling("tr"):
    ratetd=ratetd.find_next_sibling("tr") #尋找與第一列的同一層<tr>
    ratelist=[]
    for row in ratetd:
        ratelist.append(row.text)#產生除了第一列外的總利率資料
    tablelist.append(ratelist)#總利率資料加入總表
"""
寫入csv
"""
with open(csvfile,"w",encoding="utf8",newline="")as fp:
    csvwriter=csv.writer(fp)
    for row in tablelist:
        csvwriter.writerow(row)
