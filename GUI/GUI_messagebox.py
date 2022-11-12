import tkinter as tk
window=tk.Tk()
def showMsg():
    tk.messagebox.showinfo("我的對話方塊","是猴子")
btn1=tk.Button(window,text="好家在",command=showMsg)
btn1.pack() 
window.mainloop()  