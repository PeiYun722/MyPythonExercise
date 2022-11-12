# 第一種寫法
import tkinter as tk
window=tk.Tk()
# 匯入第二種寫法
"""
from tkinter import *
window=Tk()
window.mainloop() 
"""
window.title("GUI視窗") 
window.geometry("600x300")  #顯示視窗大小
window.maxsize(1000,600)    #限定視窗最大範圍

"""""""""""""""
標籤
"""""""""""""""
label1=tk.Label(window, text = "文字標籤一", width=30, bg="lightyellow")
label2=tk.Label(window, text = "文字標籤二", width=30, bg="lightblue")
label3=tk.Label(window, text = "文字標籤三", width=30, bg="lightgray")

"""""""""""""""
1.pack():置中從上放到下
"""""""""""""""
# label1.pack() 
# label2.pack()
# label3.pack()

"""""""""""""""
2.grid():可安插位置，靠左，從上往下依序擺放(row要按照順序)
"""""""""""""""
# label1.grid(row=0,column=0) 
# label2.grid(row=1,column=0)
# label3.grid(row=1,column=1)

"""""""""""""""
3.place():利用XY座標來安插位置
"""""""""""""""
# label1.place(x=0,y=0) 
# label2.place(x=50,y=50)
# label3.place(x=100,y=100)

"""""""""""""""
設定標籤字型大小
"""""""""""""""
# label4=tk.Label(window, text = "文字標籤三",
#                 bg="lightyellow",
#                 width=15,
#                 font="微軟正黑體 24 bold italic")
# label4.pack()

window.mainloop()
