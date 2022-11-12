import tkinter as tk

window=tk.Tk()
window.title("選項按鈕")

def show_selection():
    lab_result["text"]="性別:"+gender.get()
def chi_value():
    option1.set("男")
    option2.set("女")
def eng_value():  
    option1.set("male")
    option2.set("female")
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

tk.Radiobutton(window,
               variable=gender,
               textvariable=option1, #不用text的原因是因為選項是變數
               value="男(male)",
               command=show_selection).pack()
tk.Radiobutton(window,
               variable=gender,
               textvariable=option2,
               value="女(female)",
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