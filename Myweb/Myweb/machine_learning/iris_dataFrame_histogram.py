#========
#Histogram直方圖
#========

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris 
iris=load_iris() #載入iris資料集
df_data=pd.DataFrame(data=np.c_[iris["data"],iris["target"]],
                     columns=["SepalLengthCm","SepalWidthCm",
                              "PetalLengthCm","PetalWidthCm","Species"])
#製作df_data的直方圖
df_data.hist(alpha=0.6,layout=(3,3),figsize=(12,8),bins=10)
plt.tight_layout()
plt.show()