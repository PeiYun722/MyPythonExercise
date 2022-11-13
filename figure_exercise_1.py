import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
x=[0,1,2,3,4,5,6,7]
y=[-9,0,-3,9,16,25,36,49]
y2=[49,36,25,16,9,4,1,0]
plt.plot(x,y,marker="o",color="#FFC092")
plt.plot(x,y2,"-.",lw=8,color="#91F6FF")
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# plt.rcParams['axes.unicode_minus'] = False

font_prop=fm.FontProperties(fname="C:\Windows\Fonts\kaiu.ttf")
plt.xlabel("計數",size=15)
plt.ylabel("y\n軸",size=15,rotation=0)
plt.title("標題",loc="left",fontsize=25,color="r")
plt.axis([-1,10,-20,70])
plt.show()