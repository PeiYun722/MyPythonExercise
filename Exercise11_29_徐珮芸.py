"""
請撰寫一程式,用numpy做出以下的ndarray,並輸出以下資料:
    1.紅框圈起的四個角落的值
    2.黃框圈起的值
    3.計算每一排的總合
"""
import numpy as np
#製作題目規定之numpy
all=np.array([])
for i in range(6):
    temp=np.arange(10*i,10*i+6)
    all=np.r_[all,temp]
all=all.reshape(6,6)
