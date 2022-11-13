#==================
#sepal_length:花萼長度
#sepal_width:花萼寬度
#petal_length:花瓣長度
#petal_width:花瓣寬度
#species:類別
#==================

import pandas as pd
import matplotlib.pyplot as plt

fp="C:\MyPython\Myweb\machine_learning\iris.csv"
colname=["sepal_length","sepal_width","petal_length",
         "petal_width","species"]
iris=pd.read_csv(fp,names=colname)

#依類別分類資料
iris_setosa=iris[iris["species"]=="Iris-setosa"]
iris_versicolor=iris[iris["species"]=="Iris-versicolor"]
iris_virginica=iris[iris["species"]=="Iris-virginica"]

#plt.plot(X資料,Y資料,顯示樣子,顏色,標籤)
plt.plot(iris_setosa["sepal_length"],iris_setosa["sepal_width"],
          "*",color="g",label="setosa")
plt.plot(iris_versicolor["sepal_length"],iris_versicolor["sepal_width"],
          "x",color="b",label="versicolor")
plt.plot(iris_virginica["sepal_length"],iris_virginica["sepal_width"],
          ".",color="r",label="virginica")

plt.xlabel("Sepal Length")#X座標標籤
plt.ylabel("Sepal Width")#Y座標標籤
plt.title("Iris Sapal length and width anslysis")
plt.legend()#加入圖例(標籤
plt.show()