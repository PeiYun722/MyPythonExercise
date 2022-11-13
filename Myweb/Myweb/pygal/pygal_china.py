#===========
#建立中國地圖
#===========
import pygal
from pygal_maps_world.i18n import COUNTRIES
import pygal_maps_world

worldMap=pygal.maps.world.World() #建立世界地圖物件
worldMap.title="中國地圖:China in the Map" #title屬性:地圖標題
worldMap.add("China",["cn"]) #add方法:標記地區/國家
worldMap.render_to_file("C:\MyPython\country01.svg") #輸出svg圖檔