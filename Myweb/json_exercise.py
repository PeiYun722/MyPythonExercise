"""""""""
讀取json檔，並印出國家代碼、國家名稱、人口數
"""""""""
import  json
url=r"C:\Mypython\Myweb\populations.json"
with open(url,encoding="utf8") as file:
    data=json.load(file)

for getData in data:
    if getData["Year"]=="2000":
        print("國家代碼:",getData["Country Code"],
              "國家名稱:",getData["Country Name"],
              "人口數:",getData["Numbers"])
        
        
