import tkinter as tk
def showMsg():
    label1["text"]="Hello World!" #text為文字屬性，[]裡面放屬性
window=tk.Tk()
btn1=tk.Button(window,text="顯示訊息",command=showMsg) #command:按鈕按下後使用的方法
label1=tk.Label(window) #在window視窗放一個label
label1.pack()
btn1.pack() #從上到下依序放label，bottom
window.mainloop()