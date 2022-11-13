#===============
#seaborn.pairplot:成對繪圖
#               可呈現兩特徵之間的關係
#===============


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris=load_iris()
df_data=pd.DataFrame(data=np.c_[iris["data"],iris["target"]],
                     columns=["SepalLengthCm","SepalWidthCm",
                              "PetalLengthCm","PetalWidthCm","Species"])
#hue:設定分類
#diag_kind:設定對角線繪圖格式(kde:密度估計,hist:直方圖
#kind:設定非對角線圖形(scatter:散點圖,reg回歸線(直線):顯示變量之間的關係
sns.pairplot(df_data,hue="Species",height=2,diag_kind="kde")
