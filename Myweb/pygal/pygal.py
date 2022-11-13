from pygal_maps_world.i18n import COUNTRIES #COUNTRIES:模組內建國家資料

for countryCode in sorted(COUNTRIES.keys()):
    print("國家代碼:",countryCode,"\n國家名稱=",COUNTRIES[countryCode],"\n")
    
#============
#pygal模組 => 
#    SVG圖表庫Scalable Vector Graphics
#    向量圖格式，可縮放，使用瀏覽器開啟，可互動
#============

#============
#匯入模組 
#  1.pip install pygal_maps_world
#  2.pip install pygal
#============