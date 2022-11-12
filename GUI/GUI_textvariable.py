"""
part1:加法計算機
"""
import tkinter as tk

"""
建立視窗
"""
window=tk.Tk()
window.title("文字方塊元件")
"""""""""""""""""
add函式內容:
    以set方法設定result內容為取得num1,num2內容並加總
"""""""""""""""""
def add():
    result.set(num1.get()+num2.get())
    
"""""""""""""""""
textvariable:可以看作是動態版的text，文字內容隨著變數值設置而改變
以Entry元件之textvariable屬性設定為Entry元件的內容，此元件內容為num1
"""""""""""""""""
num1=tk.DoubleVar()
num2=tk.DoubleVar()
result=tk.DoubleVar()

tk.Entry(window,width=10,textvariable=num1).pack(side=tk.LEFT)
tk.Label(window,width=5,text="+").pack(side=tk.LEFT)
tk.Entry(window,width=10,textvariable=num2).pack(side=tk.LEFT)
tk.Button(window,width=5,text="=",command=add).pack(side=tk.LEFT)
tk.Entry(window,width=10,textvariable=result).pack(side=tk.LEFT)
window.mainloop()