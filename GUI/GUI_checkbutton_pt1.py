import tkinter as tk
from tkinter import messagebox as msg
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
"""""""""""""""""
建立視窗得到核取字串方法
"""""""""""""""""
def showMsg():
    result=""
    for i in checkvalue:
        if checkvalue[i].get()==True:
            result=result+dessert[i]+","
    msg.showinfo("核取結果", result)
"""""""""""""""""
建立標籤
"""""""""""""""""
label1=tk.Label(window,text="請核取您喜歡的甜點:").pack()
"""""""""""""""""
將dict(dessert)用迴圈產生Checkbutton及產生一個
"""""""""""""""""
dessert={0:"馬卡龍",1:"舒芙雷",2:"草莓塔",3:"蘋果派"}
checkvalue={}
for i in range(len(dessert)):
    checkvalue[i]=tk.BooleanVar()
    tk.Checkbutton(window,text=dessert[i],variable=checkvalue[i]).pack()
                         #text:顯示的文字  
                         #variable:，值為 1 或 0，代表選中或不選中(綁定哪個變數)
    
tk.Button(window,text="確定",command=showMsg).pack()#確定按鈕
window.mainloop()
        
        