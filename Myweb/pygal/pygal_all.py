import pygal
worldMap=pygal.maps.world.World()
worldMap.title="Asia,Europe,Africa,and North America" 
worldMap.add("Asia",["cn","jp","th"]) 
worldMap.add("Europe",["fr","de","it"]) 
worldMap.add("Africa",["eg","ug","ng"]) 
worldMap.add("North America",["ca","us","mx"]) 
worldMap.render_to_file("C:\MyPython\Myweb\pygal\country03.svg")
#add(國家or州名,國家代碼)
