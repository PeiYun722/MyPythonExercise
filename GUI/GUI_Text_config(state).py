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
text1=tk.Text(window,width=30,height=10,bg="darkorange")
text1.config(padx=5,pady=5,font="Verdana 12") #padx(y):設定元件邊框與容器距離
text1.insert(tk.INSERT,"Special cases aren't special \
             enough to break the rules.\n")
text1.pack()

"""""""""""""""""
*建立方法
"""""""""""""""""
def disable_wget():
    text1.config(state=tk.DISABLED,bg="gray",fg="gold")
                #state:設定文字區域的狀態(tk.DISABLED:僅可閱讀)
def normal_wget():
    text1.config(state=tk.NORMAL,bg="lightblue",fg="darkblue")
    
"""""""""""""""""
建立按鈕
"""""""""""""""""   
btn1=tk.Button(window,text="禁止使用",command=disable_wget)
btn1.pack(side=tk.LEFT)
btn2=tk.Button(window,text="啟用",command=normal_wget)
btn2.pack(side=tk.LEFT)
btn3=tk.Button(window,text="離開",command=window.destroy)
btn3.pack(side=tk.LEFT)

window.mainloop()