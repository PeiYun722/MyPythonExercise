def twodigit(n):
    if(n<10):
        retser="0"+str(n)
    else:
        retser=str(n)
    return retser

import requests
import json,csv
import os
import pandas as pd
import time
import matplotlib.pyplot as plt
# from fake_useragent import UserAgent
# ua=UserAgent()
# headers={"user-agent":ua.random}
plt.rcParams["font.sans-serif"]=["Microsoft JhengHei"]
urlbase="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021"
urltail="01&stockNo=2317&_=1666237051711"
filepath="C:\MyPython\Myweb\stockyear2021.csv"
if not os.path.isfile(filepath):
    for i in range(1,13):
        url_twse=urlbase+twodigit(i)+urltail
        res=requests.get(url_twse)
        jdata=json.loads(res.text)  
        
        outputfile=open(filepath,"a",newline="",encoding="utf-8-sig")
        outputwriter=csv.writer(outputfile)
        
        if i==1:
            outputwriter.writerow(jdata["fields"])
        for dataline in (jdata["data"]):
            outputwriter.writerow(dataline)
        time.sleep(0.5)
    outputfile.close()
    
pdstock=pd.read_csv(filepath,encoding="utf-8-sig")
pdstock.plot(kind="line",figsize=(12,6),x="日期",y=["收盤價","最低價","最高價"])
#=========================
#(1)全年個股資料網址由單月產生
#(2)單月網址觀察可得:data參數後即為查詢日期，由該月一日起，網址可寫到月份即可
#(3)以迴圈取得全年1~12月的資料，利用迴圈變數i執行12次，
#   i=1~12帶入單月網址中，但網址日期參數值為雙位數(十位)
#   故須將i值的個位數部分轉換為雙位數
#(4)建立函式twodigit()，當迴圈變數i為個位數時，以函式轉換為雙位數字串
#   並帶回網址中，使全年網址可透過迴圈取得，即可取得全年每月個股資料
#=========================