import pygal
worldMap=pygal.maps.world.World()
worldMap.title="Populations in China/Japan/Thailand" 
worldMap.add("Asia",{"cn":1262645000,
                     "jp":12687000,
                     "th":63155029})
worldMap.render_to_file("C:\MyPython\Myweb\pygal\country04.svg")