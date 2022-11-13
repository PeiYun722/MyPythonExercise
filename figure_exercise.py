import matplotlib.pyplot as plt
plt.figure(facecolor="#FFCEAB")#背景畫布

data={"第一筆":[2000,1000,500],"第二筆":[3000,2000,3500],"第三筆":[1100,2000,3200]}
x=[1,2,3]
y1,y2,y3=data["第一筆"],data["第二筆"],data["第三筆"]
labels=["2000年","2001年","2002年"]

plt.subplot(1,2,1)
plt.plot(x,y1,label="第一筆")
plt.xticks(x,labels)#設定X軸標籤
plt.legend(loc=9) #圖例
plt.grid() #網格

plt.subplot(1,2,2)
plt.plot(x,y2,label="第二筆")
plt.xticks(x,labels)#設定X軸標籤
plt.legend(loc=9) #圖例
plt.grid() #網格

# plt.plot(x,y3,label="第三筆")
plt.savefig("one.jpg")#儲存
plt.show()
