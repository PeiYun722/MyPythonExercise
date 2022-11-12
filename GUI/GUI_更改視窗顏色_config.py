import tkinter as tk
"""""""""""""""""
GUI元件組態設定:
    元件名.config(option=value...)
                元件屬性  屬性值
"""""""""""""""""
def yellow():
    window.config(bg="yellow")
def blue():
    window.config(bg="blue")
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("按鈕元件動作")
window.geometry("300x200")
"""""""""""""""""
建立按鈕
"""""""""""""""""
exitbtn=tk.Button(window,text="EXIT",command=window.destroy)
bluebtn=tk.Button(window,text="blue",command=blue)
yellowbtn=tk.Button(window,text="yellow",command=yellow)
"""""""""""""""""
放入元件
"""""""""""""""""
#anchor屬性:tkinter方法通常用於布置元件，功能為錨點(元件放置於其父物件的基準點)
exitbtn.pack(anchor=tk.CENTER,side=tk.RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=tk.CENTER,side=tk.RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=tk.CENTER,side=tk.RIGHT,padx=5,pady=5)

window.mainloop()