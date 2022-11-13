#=========================
#Seaborn:
#       以matplotlib為基礎之高階繪圖函式庫(套件)，
#       可視為matplotlib之補強
#=========================


import seaborn as sbn
import numpy as np
#隨機產生100000組標準常態分配資料(平均值0，標準差1)
nor_sample=np.random.normal(size=100000)
sbn.displot(nor_sample) #distribution plots 分布圖