import requests
import json,csv
import os
import pandas as pd
import matplotlib.pyplot as plt
filepath="C:\MyPython\Myweb\stockmonth09.csv"
#若繪圖有亂碼，則加入這行
plt.rcParams["font.sans-serif"]=["Microsoft JhengHei"]

if not os.path.isfile(filepath):
    url_twse="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220901&stockNo=2317&_=1666237252190"
    res=requests.get(url_twse)
    jdata=json.loads(res.text)
    outputfile=open(filepath,"w",newline="",encoding="utf-8-sig")
    outputwriter=csv.writer(outputfile)
    outputwriter.writerow(jdata["fields"])
    for dataline in (jdata["data"]):
        outputwriter.writerow(dataline)
    outputfile.close()
    
pdstock=pd.read_csv(filepath,encoding="utf-8-sig")
pdstock.plot(kind="line",figsize=(12,6),x="日期",y=["收盤價","最低價","最高價"])