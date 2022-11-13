#==================
#scikit-learn:(sklearn)
#           Python中機器學習的函式庫
#           搭配Numpy格式的資料
#           轉換為Pandas中之DataFrame
#==================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris 
iris=load_iris() #載入iris資料集
x=iris.data #data->屬性，為原始輸入資料，機器學習資料的原始特徵
y=iris.target #目標，輸出
iris=load_iris()

#==================
#np.c_:是按行連接兩個矩陣，就是把兩矩陣左右相加，要求行数相等
#columns:輸出的欄位
#==================
df_data=pd.DataFrame(data=np.c_[iris["data"],iris["target"]],
                     columns=["SepalLengthCm","SepalWidthCm",
                              "PetalLengthCm","PetalWidthCm","Species"])
print(iris)