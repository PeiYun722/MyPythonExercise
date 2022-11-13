import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris=load_iris()
df_data=pd.DataFrame(data=np.c_[iris["data"],iris["target"]],
                     columns=["SepalLengthCm","SepalWidthCm",
                              "PetalLengthCm","PetalWidthCm","Species"])
fig,axes=plt.subplots(nrows=1,ncols=4)
fig.set_size_inches(15,4)
sns.histplot(df_data["SepalLengthCm"][:],ax=axes[0],kde=True)
sns.histplot(df_data["SepalWidthCm"][:],ax=axes[1],kde=True)
sns.histplot(df_data["PetalLengthCm"][:],ax=axes[2],kde=True)
sns.histplot(df_data["PetalWidthCm"][:],ax=axes[3],kde=True)

#==============
#kde:密度估計曲線
#　　功用：(1)觀察某特徵分布的情況
#　　　　　(2)觀察特徵間的關聯性
#==============