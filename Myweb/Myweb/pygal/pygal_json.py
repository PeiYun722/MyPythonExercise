import json
import pygal
from pygal.maps.world import COUNTRIES

#=======================================
#getCountryCode函式:搜尋國家名稱及代碼，若與帶入的名稱相等，則傳回該
#                   國家代碼，否則傳回None
#COUNTRIES.items():dict_items([('ad', 'Andorra'),.....
#=======================================
def getCountryCode(countryName):
    for dictCode,dictName in COUNTRIES.items(): 
        if dictName == countryName:
            return dictCode
    return None

#=======================================
#讀取json檔
#=======================================
fn="C:\MyPython\Myweb\pygal\population_data(2010).json"
with open(fn) as fnObj:
    getDatas=json.load(fnObj)

#=======================================
#以for迴圈篩選json檔(getDatas)中的2000年數據
#=======================================
dictData={} #建立地圖空字典
for getData in getDatas:
    if getData["Year"]=="2000":
        countryName=getData["Country Name"]
        countryCode=getCountryCode(countryName)
        population=int(float(getData["Value"]))
        
        #只要getCountryCode函式不傳回None，則國家代碼將人口數加入字典
        if countryCode!= None:
            dictData[countryCode]=population


worldMap=pygal.maps.world.World()
worldMap.title="2000年世界人口:World Population in 2000" #標題
worldMap.add("Year 2000",dictData) 
worldMap.render_to_file("C:\MyPython\Myweb\pygal\country05.svg")