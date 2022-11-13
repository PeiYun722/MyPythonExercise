import matplotlib.pyplot as plt
import numpy as np
plt.figure(facecolor="#FFEB91")

"""
長條圖
"""
# name=["小明","小華","小芳"]
# score=[100,80,90]
# plt.bar(name,score,color="#9192FF")
# plt.show()

"""
圓餅圖
"""
# area=["台灣","中國","香港"]
# people=[70,10,30]
# color=["#EB8FA4","#E8C9FF","#ACBCE8"]
# exp=[0.0,0.1,0.0]
# plt.pie(people,labels=area,autopct="%d%%",colors=color,explode=exp,shadow=True)
# plt.title("隨便寫的標題",fontsize=15)
# plt.legend(prop={"size":9})
# plt.show()
"""
散點圖
"""
x=np.arange(1,21)
y=np.random.randint(1,10,20)