import tkinter as tk
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("文字區域應用")
window.geometry("500x300")

"""""""""""""""""
建立標籤
"""""""""""""""""
text1=tk.Text(window,width=50,height=10,bg="darkorange")
text1.config(padx=5,pady=5,font="Verdana 12") 
text1.insert(tk.INSERT,"Hello world!\n")
text1.insert(tk.INSERT,"Beautiful is better than ugly.")
text1.insert(tk.INSERT,"Explicit is better than implicit.\n")
text1.insert(tk.INSERT,"Simple is better than complex.\n")
text1.insert(tk.INSERT,"Complex is better than complicated.\n")
text1.insert(tk.INSERT,"Flat is better than nested.\n")
text1.insert(tk.INSERT,"Sparse is better than dense.\n")
text1.insert(tk.INSERT,"Readability counts.\n")
text1.insert(tk.INSERT,"Special cases aren't special enough to break the rules.\n")     

text1.pack()

"""""""""""""""""
*建立刪除方法
delete(from, to):刪除字元索引 from 到 to 之間的字元 (不含 to)
"""""""""""""""""
def delete_all():
    text1.delete(1.0,tk.END) #tk.END="end"
def delete_first():
     text1.delete(1.0,2.0) 
                #(1.0,"1.end")->不包含換行字元，所以會多一行
#文字區域內的索引位置:
#  ->文字區域內字元位置配置方式:列.欄
#    計算方式:以數值方式標示->列數值.欄數值
#    列數值從1起算，欄數值從0起算
#    計算方向:由左往右，由上而下
#    例如:左上角第一個字元:1.0、第二列第三行:2.2、第一列最後一個字元:"1.end"
    
"""""""""""""""""
建立按鈕
"""""""""""""""""   
btn1=tk.Button(window,text="刪除全部",command=delete_all)
btn1.pack(side=tk.LEFT)
btn2=tk.Button(window,text="刪除第一列",command=delete_first)
btn2.pack(side=tk.LEFT)
btn3=tk.Button(window,text="離開",command=window.destroy)
btn3.pack(side=tk.LEFT)

window.mainloop()