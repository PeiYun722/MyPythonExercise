"""
part2:增加Button功能為關閉視窗
"""

import tkinter as tk
def msgShow():
    label1["text"]="I'm Button."
    label1["bg"]="lightgray"
    label1["fg"]="red"
        
window=tk.Tk() 
label1=tk.Label(window)
btn1=tk.Button(window,text="Message",width=8,command=msgShow)
btn2=tk.Button(window,text="Exit", width=8,command=window.destroy)
label1.pack()
btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)
window.mainloop() 
