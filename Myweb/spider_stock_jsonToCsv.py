import requests
import json,csv
import os
filepath="C:\MyPython\Myweb\stockmonth09.csv"#儲存下載的個股資料之CVS檔案
#=========================
#if 條件式:
#       (1)判斷檔案filepath是否存在
#       (2)以requests.get()取得個股網頁資料(為JSON格式)
#       (3)載入並解析JSON檔案
#       (4)開啟CSV檔案
#       (5)將解析的JSON檔案寫入CSV檔案
#=========================
if not os.path.isfile(filepath):
    url_twse="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220901&stockNo=2317&_=1666237252190"
    res=requests.get(url_twse)
    jdata=json.loads(res.text)
    outputfile=open(filepath,"w",newline="",encoding="utf-8-sig")
    outputwriter=csv.writer(outputfile)
    outputwriter.writerow(jdata["fields"])#寫標題
    for dataline in (jdata["data"]):#寫資料
        outputwriter.writerow(dataline)
    outputfile.close()
    
#==============
#url_twse
#   1.(Network-> STOCK_DAY?.....-> Copy ->Copy link address)
#   2.(Network -> Headers -> Request URL)
#==============