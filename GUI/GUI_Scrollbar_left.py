"""""""""""""""""
左側卷軸
"""""""""""""""""
import tkinter as tk
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("右側卷軸")
window.geometry("480x240")

scb1=tk.Scrollbar(window)
scb1.pack(side=tk.LEFT,fill=tk.Y)
text1=tk.Text(window,height=10,bg="pink")
text1.config(padx=5,pady=5,font="Verdana 12")
text1.config(yscrollcommand=scb1.set) 
scb1.config(command=text1.yview) 
str="Simple is better than complex!\nFlat is better than nested!"
strlist=[]
for i in range(10):
   strlist.append(str)
text1.insert(tk.INSERT,'\n'.join(strlist))
text1.pack(side=tk.RIGHT,fill=tk.Y)
window.mainloop()
