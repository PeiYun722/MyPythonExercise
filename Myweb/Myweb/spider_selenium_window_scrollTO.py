from selenium import webdriver
import time
driver_path=r"C:\MyPython\Myweb\chromedriver\chromedriver"
url=r"https://www.104.com.tw/jobs/search/?ro=0&\
    keyword=Python&expansionType=area,spec,com,job,wf,wktm\
    &jobsource=2018indexpoc&langFlag=0&\
    langStatus=0&recommendJob=1&hotJob=1"

driver=webdriver.Chrome(driver_path)
driver.implicitly_wait(10)
driver.get(url)
print("-"*20)
print(driver.title)
print(len(driver.page_source))#page_source網頁原始碼

for x in range(5):
    #window.scrollTo(起點,終點):網頁視覺元件卷軸捲動的範圍
    #document.body.scrollHeight:網頁主體(即視窗)的捲動高度
    js="window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)#等3秒後再載入
    print(x+1,len(driver.page_source))
driver.quit()