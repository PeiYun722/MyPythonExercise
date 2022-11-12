"""
part4:輸入帳號密碼後，後面文字方塊清空
"""
import tkinter as tk
"""""""""""""""""
建立列印方法
"""""""""""""""""
def printInfo():
    print("帳號:%s \n密碼:%s"%(e1.get(),e2.get()))
    e1.delete(0,tk.END) #設定執行完並刪除
    e2.delete(0,tk.END)
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("文字方塊元件")
"""""""""""""""""
建立標籤
"""""""""""""""""
lab1=tk.Label(window,text="帳號:")
lab2=tk.Label(window,text="密碼")
"""""""""""""""""
建立輸入框
"""""""""""""""""
e1=tk.Entry(window)
e2=tk.Entry(window,show="*")
e1.insert(0, "Simon") #設預設值
e2.insert(0, "12345") #設預設值
"""""""""""""""""
建立按鈕
"""""""""""""""""
btn1=tk.Button(window,text="print",command=printInfo)
btn2=tk.Button(window,text="Exit",command=window.destroy)
"""""""""""""""""
放入元件
"""""""""""""""""
lab1.grid(row=0,column =0)
lab2.grid(row=1,column =0)
e1.grid(row=0,column =1)
e2.grid(row=1,column =1)
btn1.grid(row=2,column =0)
btn2.grid(row=2,column =1)

window.mainloop()