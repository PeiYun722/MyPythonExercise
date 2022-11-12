#GUI_checkbutton_pt2 迴圈版本
import tkinter as tk
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("Checkbutton元件")

"""""""""""""""""
建立方法
"""""""""""""""""
def show_sel():
    selection=[]
    for i in range(len(program)):
        if checkvar[i].get()==True:
            selection.append(program[i])
    result.config(text="選取結果:"+",".join(selection))    
        
"""""""""""""""""
建立最上方標籤
"""""""""""""""""
tk.Label(window,text="程式語言:",width=30,background="cyan").pack()

"""""""""""""""""
用迴圈建立checkbutton
"""""""""""""""""
program=["Java","Python","C++"]
checkvar=[]
for i in range(len(program)):
    checkvar.append(tk.BooleanVar())
    tk.Checkbutton(window,text=program[i],variable=checkvar[i],command=show_sel).pack()
    
"""""""""""""""""
建立顯示標籤
"""""""""""""""""
result=tk.Label(window,text="選取結果:",width=30,background="darkorange")
result.pack() #pack不能放在上列

window.mainloop()