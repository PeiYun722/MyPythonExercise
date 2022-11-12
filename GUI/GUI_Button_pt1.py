"""
part1:按鈕觸發標籤動作
"""

import tkinter as tk
def msgShow():
    label1["text"]="I'm Button."
    label1["bg"]="lightgray"
    label1["fg"]="red"
        
window=tk.Tk() 
label1=tk.Label(window)
btn1=tk.Button(window,text="Message",command=msgShow)
label1.pack()
btn1.pack()
window.mainloop() 