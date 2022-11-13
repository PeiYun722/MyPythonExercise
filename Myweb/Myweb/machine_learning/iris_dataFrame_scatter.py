#===================
#scatter_matrix(散點圖)
#===================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from pandas.plotting import scatter_matrix
iris=load_iris()
df_data=pd.DataFrame(data=np.c_[iris["data"],iris["target"]],
                     columns=["SepalLengthCm","SepalWidthCm",
                              "PetalLengthCm","PetalWidthCm","Species"])
#figsize:框格大小
#diagonal:"kde"(密度估計)or"hist"(直方圖)
scatter_matrix(df_data,figsize=(10,10),color="b",diagonal="kde")
