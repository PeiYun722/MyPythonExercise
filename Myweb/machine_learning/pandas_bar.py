#=====================
#直條圖(柱狀圖):
#   用途:比較各類別資料
#       呈現資料在特定時間範圍內的變化
#=====================
import pandas as pd
import matplotlib.pyplot as plt
fp="C:\MyPython\Myweb\machine_learning\iris.csv"

colname=["sepal_length","sepal_width","petal_length",
         "petal_width","species"]
iris=pd.read_csv(fp,names=colname)
#=====================
#以鳶尾花的類別分組並統計均值
#=====================
iris_mean=iris.groupby("species",as_index=False).mean()

iris_mean.plot(kind="bar")#直條圖
#=====================
#xticks類似覆蓋，而且覆蓋的數組長度要和原来坐標長度一致
#將原來iris_mean的index(1,2,3)資料改為iris_mean的species資料
#=====================
plt.xticks(iris_mean.index,iris_mean["species"],rotation=0)
plt.show()

#==================
#sepal_length:花萼長度
#sepal_width:花萼寬度
#petal_length:花瓣長度
#petal_width:花瓣寬度
#species:類別
#==================