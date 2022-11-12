"""
請撰寫一程式,用numpy做出以下的ndarray,並輸出以下資料:
    1.紅框圈起的四個角落的值
    2.黃框圈起的值
    3.計算每一排的總合
"""
import numpy as np
#製作題目規定之numpy
all=np.arange(0,36).reshape(6,6)
for i in range(6):
    for j in range(6):
        all[i][j]=i*10+j
print(all)

print("四個角落")
print(all[::5,::5])
print("-"*20)
print(all[2:4,3:5])
print("-"*20)
print("每一行總和")
for i in range(len(all)):
    print("第%d排:"%(i+1),end="")
    print(np.sum(all[i]))