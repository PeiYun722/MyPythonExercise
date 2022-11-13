import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris 
iris=load_iris() #載入iris資料集
x=iris.data #data->屬性，為原始輸入資料，機器學習資料的原始特徵
y=iris.target #目標，輸出
iris=load_iris()

df_data=pd.DataFrame(data=np.c_[iris["data"],iris["target"]],
                     columns=["SepalLengthCm","SepalWidthCm",
                              "PetalLengthCm","PetalWidthCm","Species"])

df_data.hist(alpha=0.6,layout=(3,3),figsize=(12,8),bins=10)
plt.tight_layout()
plt.show()