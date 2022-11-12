"""
selenium應用實作:
    1.自動登入facebook
    2.中央氣象局今日氣溫(如台北市,新北市...)
"""
from selenium import webdriver
#driver_path:設定chromedriver完整檔案路徑
driver_path= "C:\MyPython\Myweb\chromedriver\chromedriver"

#以driver_path執行webdriver.Chrome(driver_path)建立瀏覽器物件driver
driver=webdriver.Chrome(driver_path)

#以driver執行get()方法連結要開啟的網址(自動開啟瀏覽器)
driver.get("http://www.google.com")

driver.quit() #關閉瀏覽器
