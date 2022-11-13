"""
實作2:將摩根台股指數之JSON資料，擷取後存檔為CSV格式
"""
import requests
import json ,csv
csvfile="tw_sgx.csv"
url="https://api.sgx.com/derivatives/v1.0/contract-code/\
TWN?order=asc&orderby=delivery-month&category=futures&\
session=-1&t=1665296738306"
r=requests.get(url)

json_data=json.loads(r.text)
output=[]
for data in json_data["data"]:
    item=[]
    item.append(data["last-update-time"])
    item.append(data["last-trading-date"])
    item.append(data["symbol"])
    if data["current-trading-session"]=="0":
        item.append("T")
    else:
        item.append("T+1")
    item.append(data["change-abs"])
    item.append(data["change-percentage"])
    item.append(data["session-open-abs"])
    item.append(data["session-traded-high-abs"])
    item.append(data["session-traded-low-abs"])
    item.append(data["last-traded-price-abs"])
    item.append(data["daily-settlement-price-abs"])
    item.append(data["total-volume"])
    item.append(data["open-interest"])
    output.append(item)
    
"""
open(fp,"w"):寫入(若檔案已存在，先將其內容刪除，會覆蓋原先所有內容)
open(fp,"w+"):同"w"，但同時也可以讀取
"""
with open(csvfile,"w+",newline="") as fp:
    writer=csv.writer(fp)
    writer.writerow(["last-update-time","last-trading-date","symbol",
                      "current-trading-session","change-abs",
                      "change-percentage","session-open-abs",
                      "session-traded-high-abs","session-traded-low-abs",
                      "last-traded-price-abs","daily-settlement-price-abs",
                      "total-volume","open-interest"])
    for row in output:
        writer.writerow(row)
    
        