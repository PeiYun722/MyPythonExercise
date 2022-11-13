#=====================
#堆疊直條圖:
#   用途:比較各個項目之間的差異與其之間的關係
#=====================

import pandas as pd
import matplotlib.pyplot as plt
fp="C:\MyPython\Myweb\machine_learning\iris.csv"

colname=["sepal_length","sepal_width","petal_length",
         "petal_width","species"]
iris=pd.read_csv(fp,names=colname)

iris["species"]=iris["species"].apply(lambda x: x.replace("Iris-",""))
iris_mean=iris.groupby("species",as_index=False).mean()
iris_mean.plot(kind="barh",stacked=True)
plt.yticks(iris_mean.index,iris_mean["species"],rotation=0)
plt.show()