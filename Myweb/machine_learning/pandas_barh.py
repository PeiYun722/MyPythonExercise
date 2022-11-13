#=====================
#橫條圖:
#   用途:比較各個項目之間的差異與其之間的關係
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

iris_mean.plot(kind="barh")#直條圖
plt.yticks(iris_mean.index,iris_mean["species"],rotation=0)
plt.show()

#==================
#sepal_length:花萼長度
#sepal_width:花萼寬度
#petal_length:花瓣長度
#petal_width:花瓣寬度
#species:類別
#==================