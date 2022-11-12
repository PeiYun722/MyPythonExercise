"""""""""""""""""
卷軸
"""""""""""""""""
import tkinter as tk
window=tk.Tk()
window.title("文字區域")

song="Cause I-I-I'm in the stars tonight,\
So watch me bring the fire and set the night alight (hey)\
Shining through the city with a little funk and soul\
So I'ma light it up like dynamite, whoa oh oh"

""""
text換行方式"warp="參數", 
參數內容:.tk.CHAR (預設)=字元, tk.WORD=字, tk.NONE=不換行
"""
sbar1=tk.Scrollbar(window)
text1=tk.Text(window,height=4,width=40,wrap=tk.WORD)
text1.insert(tk.END, "Dynamite\n")
text1.insert(tk.END, song)

#fill:填滿所分配空間之方向 : NONE (預設), X, Y, BOTH
sbar1.pack(side=tk.RIGHT,fill=tk.Y)
text1.pack(side=tk.LEFT,fill=tk.Y)

sbar1["command"]=text1.yview
text1["yscrollcommand"]=sbar1.set

window.mainloop()