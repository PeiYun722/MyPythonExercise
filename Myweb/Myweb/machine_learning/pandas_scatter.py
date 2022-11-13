#=====================
#散點圖(氣泡圖):
#   用途:表達變量之間的關係
#       顯示兩個變量數值的點
#       檢測兩個變量之間是否存在關聯
#=====================

import pandas as pd
import matplotlib.pyplot as plt
fp="C:\MyPython\Myweb\machine_learning\iris.csv"

colname=["sepal length","sepal width",
         "petal length","petal width","species"]
iris=pd.read_csv(fp,names=colname)#讀檔

iris.plot(x="sepal length",y="sepal width",kind="scatter")#散點圖:scatter
plt.xlabel("Sepal Length")#X座標標籤
plt.ylabel("Sepal Width")#Y座標標籤
plt.title("Iris Sapal length and width anslysis")#標題
plt.grid()#格線
plt.show()

#==================
#sepal_length:花萼長度
#sepal_width:花萼寬度
#petal_length:花瓣長度
#petal_width:花瓣寬度
#species:類別
#==================