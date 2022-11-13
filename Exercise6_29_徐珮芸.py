# 請撰寫一程式，請使用者輸入3個整數，
# 將這3個整數傳入自訂函數後，
# 請計算一元二次方程式答案
import math

def judge(a,b,c):
    if ((b**2)-4*a*c)>0:
        ans=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
        ans2=(-b-math.sqrt((b**2)-4*a*c))/(2*a)
        print("答案為:",ans,",",ans2)
    elif (b**2-4*a*c)==0:
         ans=-b/(2*a)
         print("答案為:",ans)
    else:
         print("無解")

#使用者輸入
a=input("請輸入a:")
b=input("請輸入b:")
c=input("請輸入c:")
#轉型成數值
a=int(a)
b=int(b)
c=int(c)
#呼叫函數
judge(a,b,c)
    
    
