from selenium import  webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

def returnAiPicture(userinput):
    driver_path=r"C:\MyPython\Myweb\chromedriver\chromedriver"
    url=r"https://stabilityai.us.auth0.com/u/login?state=hKFo2SBZaWJTeFZhZUZ5TEZsTVNIcldGdHl6VGl5UUNwb0h3QaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFdOSmMtU214Q2MyMHlSSlJ6SFN0X0NJQ3dXcW02T0lDo2NpZNkgS3ZZWkpLU2htVW9PalhwY2xRbEtZVXh1Y0FWZXNsSE4/"
    email=r"programingaa123@gmail.com"
    password="vul3au/6"
     
    driver=webdriver.Chrome()
    driver.get(url)
        
    time.sleep(2)
    
    #登入
    driver.find_element("name","username").send_keys(email)
    driver.find_element("name","password").send_keys(password)
    driver.find_element("name","action").click() #click():按下按鈕
    time.sleep(2)
        # el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element("class name","el-button"))
        # assert el.text == "Hello from JavaScript!"
        
    driver.find_element("class name","el-button").click()
    #搜索   
    driver.find_element("id","prompt-input").click()
    driver.find_element("id","prompt-input").send_keys(Keys.CONTROL,"a")
    driver.find_element("id","prompt-input").send_keys(Keys.DELETE)
    driver.find_element("id","prompt-input").send_keys(userinput)
    driver.find_element("id","prompt-btn").click()
    time.sleep(8)
    
returnAiPicture("dog with cake")