"""
EX:製作BMI計算機
"""
import tkinter as tk
window=tk.Tk()
window.title("BMI計算機")
"""
建立方法

"""
def showMsg():
    BMI=weight.get()/((high.get()/100)**2)
    if BMI>=35:
        text="重度肥胖"
    elif BMI>=30:
        text="中度肥胖"
    elif BMI>=27:
        text="輕度肥胖"
    elif BMI>=24:
        text="過重"
    elif BMI>=18.5:
        text="健康體位"
    elif BMI<18.5:
        text="體重過輕"
    str1.set("BMI指數為:%.2f,\n您的身體質量指數為『%s』"%(BMI,text))

"""
建立label、Entry
"""
lab1=tk.Label(window,text="身高(公分):").grid(row=0,column=0)
lab2=tk.Label(window,text="體重(公斤):").grid(row=1,column=0)
high=tk.DoubleVar()
high.set(0)
weight=tk.DoubleVar()
weight.set(0)

ans1=tk.Entry(window,textvariable=high)
ans1.grid(row=0,column=1)
ans2=tk.Entry(window,textvariable=weight)
ans2.grid(row=1,column=1)
"""
建立button(計算、離開)
"""
btn1=tk.Button(window,text="計算BMI",command=showMsg).grid(row=3,column=0,sticky=tk.W)
btn2=tk.Button(window,text="Exit",command=window.destroy).grid(row=3,column=1,sticky=tk.W)
"""
建立顯示窗格
"""
str1=tk.StringVar()
lab1=tk.Label(window,bg="pink",height=2,textvariable=str1)
lab1.grid(row=4,columnspan=2,sticky=tk.W+tk.E)
"""
排版
"""

window.mainloop()
