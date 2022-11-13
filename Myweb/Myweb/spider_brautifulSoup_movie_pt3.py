"""
實作2:yahoo電影新片編號，中英文片名,(圖片)海報網址,預告片網址
"""
import  requests
from bs4 import BeautifulSoup
url="https://movies.yahoo.com.tw/movie_thisweek.html"
htmlfile=requests.get(url)
soup=BeautifulSoup(htmlfile.text,"lxml")
items=soup.find_all("div","release_info")
movieID=0
movies=[]
for item in items:
    movieID+=1
    chmovie=item.find("div","release_movie_name").a.text.strip()
    enmovie=item.find("div","en").a.text.strip()
    #find_previous_sibling():在同一層往前尋找特定節點("release_foto"和"release_info"在同一層)
    photo=item.find_previous_sibling("div","release_foto").a.img["data-src"]
    video=item.find("div","release_btn color_btnbox").find_all("a")[1]
    if "href" in video.attrs:
        video=video["href"]
    else:
        video=""    
    print("新片編號:",movieID)
    print("中文片名:",chmovie)
    print("英文片名:",enmovie)
    print("海報網址:",photo)
    print("預告片:",video)
    print()