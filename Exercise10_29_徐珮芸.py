"""
請撰寫一程式，請讀取youbike_immediate.json檔案，
並找出位於松山區youbike站的第6~10筆資料
"""
import json
infp=r"youbike_immediate.json"
with open(infp,encoding="utf8") as file:
    data=json.load(file)

ans=[]
for i in range(len(data)):
    if data[i]["sarea"]=="松山區":
        ans.append(data[i]) 

print("位於松山區的youbike站有%d站"%len(ans))
for i in range(5,10):
    print(ans[i]["sna"])