import tkinter as tk
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
"""""""""""""""""
建立標籤
"""""""""""""""""
text1=tk.Text(window,width=25,height=5)
text1.pack()
"""""""""""""""""
Text方法:tag_config(標籤名稱,屬性=值,...)
        設定文字標籤，使用於insert方法中
        insert(插入位置,文字內容,["文字標籤"])
"""""""""""""""""
text1.tag_config('tag_1',background="darkorange",foreground="blue")
text1.insert(tk.END,"I love")
text1.insert(tk.END,"Python so much.","tag_1")

window.mainloop()