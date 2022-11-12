#加入第三個選項按鈕(多元,multi)
import tkinter as tk

window=tk.Tk()
window.title("選項按鈕")

def show_selection():
    lab_result["text"]="性別:"+gender.get()
def chi_value():
    option1.set("男")
    option2.set("女")
    option3.set("多元")
def eng_value():  
    option1.set("Male")
    option2.set("Female")
    option3.set("Multi-sex")
"""""""""""""""""
建立label
"""""""""""""""""
lab1=tk.Label(window,text="性別:",width=30,bg="PaleTurquoise").pack()

"""""""""""""""""
建立var
"""""""""""""""""
gender=tk.StringVar()
gender.set("none")

"""""""""""""""""
建立radiobuttons
"""""""""""""""""
option1=tk.StringVar()
option1.set("男")
option2=tk.StringVar()
option2.set("女")
option3=tk.StringVar()
option3.set("多元")

tk.Radiobutton(window,
               variable=gender,
               textvariable=option1,
               value="男(Male)",
               command=show_selection).pack()
tk.Radiobutton(window,
               variable=gender,
               textvariable=option2,
               value="女(Female)",
               command=show_selection).pack()
tk.Radiobutton(window,
               variable=gender,
               textvariable=option3,
               value="多元(Multi-sex)",
               command=show_selection).pack()

"""""""""""""""""
建立button
"""""""""""""""""
tk.Button(window,text="中文",command=chi_value).pack(side=tk.LEFT)
tk.Button(window,text="英文",command=eng_value).pack(side=tk.RIGHT)
"""""""""""""""""
建立label
"""""""""""""""""
lab_result=tk.Label(window,text="性別:",width=30,bg="darkorange")
lab_result.pack()


window.mainloop()