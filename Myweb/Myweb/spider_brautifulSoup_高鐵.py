"""
實作三:台灣高鐵擷取所有中文英文站名
"""
"""
網頁分析:
    進入高鐵網站 > 購票資訊 > 快速查詢 > 時刻表與票價查詢
    於起程站名上按右鍵 > 檢查 >
    展開<select....>標籤(為分析項目 > find>即<select>下所有的option>) >
    可見到每一個中文站名為<option>標籤所作用的文字，
    英文站名為<option>標籤的value屬性值
"""
import requests
from bs4 import BeautifulSoup
url="https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c"
html=requests.get(url)
soup=BeautifulSoup(html.text,"lxml")
stations=soup.find("select",id="select_location01").find_all("option")
print("台灣高鐵所有中文與英文站名:")
for station in stations:
    print(station.text.strip(),":",station["value"])
    
    
"""
strip(指定要刪除的字符集的字符串):從左側和右側刪除字符，
    如果字符未提供參數，則從字符串中刪除所有前導和尾隨空格。
"""
    