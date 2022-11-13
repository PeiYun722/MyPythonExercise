#=====================
#程式二:以CSV檔案讀取後顯示該資料庫
#=====================
import pandas as pd

fp="C:\MyPython\Myweb\machine_learning\iris.csv"

colname=["sepal length","sepal width",
         "petal length","petal width","species"]
iris=pd.read_csv(fp,names=colname)
print("iris資料及長度:",len(iris))
print(iris)

#==================
#sepal_length:花萼長度
#sepal_width:花萼寬度
#petal_length:花瓣長度
#petal_width:花瓣寬度
#species:類別
#==================
