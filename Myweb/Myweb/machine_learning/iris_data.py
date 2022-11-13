#=====================
#程式一，下載並儲存儲存iris資料集為CSV格式
#=====================
import requests
url="http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
try:
    htmlfile=requests.get(url)
    print("下載成功")
except Exception as err:
    print("下載失敗")
    
fn="C:\MyPython\Myweb\machine_learning\iris.csv"
with open (fn,"wb") as fileobj:
    for diskstorage in htmlfile.iter_content(10240):
        size=fileobj.write(diskstorage)