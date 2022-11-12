"""
selenium應用實作:
    2.中央氣象局今日氣溫(如台北市,新北市...)
"""
from selenium import webdriver
from bs4 import BeautifulSoup

url=r"https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=65"
driver_path=r"C:\myPython\Myweb\chromedriver\chromedriver"
driver=webdriver.Chrome(driver_path)

"""
river.implicitly_wait():隱含等待，尋找元素時，若未能及時發現，
則等待一段時間，時間單位為秒，預設為0秒。
"""
driver.implicitly_wait(10)

driver.get(url)

#driver.page_source:取得目前的來源網頁，即以get()方法取得網頁內容
soup=BeautifulSoup(driver.page_source,"lxml")

"""
#html屬性是用空格隔開，原始碼class="tem-C is-active"，
tem-C與is-active是兩個屬性
"""
span=soup.select_one("span.tem-C.is-active")
print("今日白天氣溫:",span.text,"度")


