import json
from pygal_maps_world.i18n import COUNTRIES
def getCountryCode(countryName):
    for dictCode, dictName in COUNTRIES.items():
        if dictName ==  countryName:
            return dictCode
    return None

fn=r"C:\MyPython\Myweb\population_data(2010).json"
with open(fn) as fnObj:
    getDatas=json.load(fnObj)
for getData in getDatas:
    if getData["Year"]=="2000":
        countryName=getData["Country Name"]
        countryCode=getCountryCode(countryName)
        population=int(float(getData["Value"]))
        if countryCode != None:
            print(countryCode,":",population)
        else:
            print(countryName,":名稱不吻合")