#===========
#建立亞洲地圖
#===========
import pygal
worldMap=pygal.maps.world.World()
worldMap.title="亞洲地圖:China/Japan/Thailand" 
worldMap.add("Asia",["cn","jp","th"]) 
worldMap.render_to_file("C:\MyPython\Myweb\pygal\country02.svg")