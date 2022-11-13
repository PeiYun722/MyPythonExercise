"""
selenium應用實作:
    1.自動登入facebook
"""
from selenium import  webdriver
driver_path=r"C:\MyPython\Myweb\chromedriver\chromedriver"
url=r"https://facebook.com/"
email=r"w22835247@yahoo.com.tw"
password="vm6qo4mp6"

driver=webdriver.Chrome(driver_path)
driver.maximize_window()#瀏覽器視窗最大化
driver.get(url)

"""
driver.find_element("name","email"):搜尋元素名稱為name，值為email的元素。
.send_keys(email):將設定的email變數(程式中的電子郵件)傳送到該元素中
"""
driver.find_element("name","email").send_keys(email)

driver.find_element("name","pass").send_keys(password)
driver.find_element("name","login").click() #click():按下按鈕

