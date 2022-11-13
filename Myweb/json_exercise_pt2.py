import json
fp=r"C:\MyPython\Myweb\population_data(2010).json"
with open(fp,encoding="utf8") as jsonfile:
    getDatas=json.load(jsonfile)

for getData in getDatas:
    if getData["Year"]=="2000":
        countryName=getData["Country Name"]
        countryCode=getData["Country Code"]
        population=getData["Value"]
        print("國家代碼 = ",countryCode,"\t國家名稱 = ",countryName,"\t人口數 = ",population)    