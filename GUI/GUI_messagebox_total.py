import tkinter as tk
from tkinter import messagebox as msg

def shinfo():
    msg.showinfo("showinfo","This is showinfo.")
def shwarning():
    msg.showwarning("showwarning","This is showwarning.")
def sherror():
    msg.showerror("showerror","This is showerror.")
def askyn():
    msg.askyesno("askyesno","This is askyesno.")
def askokcel():
    msg.askokcancel("askokcancel","This is askokcancel.")
def askyncel():
    msg.askyesnocancel("askyesnocancel","This is askyesnocancel.")
def askque():
    msg.askquestion("askquestion","This is askquestion.")
def askrtcel():
    msg.askretrycancel("askretrycancel","This is askretrycancel.")
window=tk.Tk()
window.title("測試")
tk.Button(window,text="showinfo",command=shinfo).grid(row=0,column=0)
tk.Button(window,text="showwarning",command=shwarning).grid(row=0,column=1)
tk.Button(window,text="showerror",command=sherror).grid(row=0,column=2)
tk.Button(window,text="askyesno",command=askyn).grid(row=0,column=3)
tk.Button(window,text="askokcancel",command=askokcel).grid(row=1,column=0)
tk.Button(window,text="askyesnocancel",command=askyncel).grid(row=1,column=1)
tk.Button(window,text="askquestion",command=askque).grid(row=1,column=2)
tk.Button(window,text="askretrycancel",command=askrtcel).grid(row=1,column=3)

window.mainloop()    