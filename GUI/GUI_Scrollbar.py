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

"""
text換行方式"warp="參數", 
參數內容:.tk.CHAR (預設)=字元, tk.WORD=字, tk.NONE=不換行
"""
sbar1=tk.Scrollbar(window)
text1=tk.Text(window,height=4,width=40,wrap=tk.WORD)
text1.insert(tk.END, "Dynamite\n")
text1.insert(tk.END, song)

#fill:填滿所分配空間之方向 : NONE (預設), X, Y, BOTH
sbar1.pack(side=tk.RIGHT,fill=tk.Y)#滾軸由右往左排對齊且填滿Y軸
text1.pack(side=tk.LEFT,fill=tk.Y)
"""
參數 xscrollcommand與 yscrollcommand
是用來綁定 (呼叫) Scrollbar 元件的 set() 方法的, 
這樣就可以為 Text 元件加上捲軸了. 
不過這種綁定是雙向的, 
在 Scrollbar 元件上還必須設定其 command 參數
來呼叫 Text 元件的 xview() 或 yview() 方法, 
這樣當捲動 Scrollbar 時 Text 元件的內容才會同步捲動
"""
sbar1["command"]=text1.yview
text1["yscrollcommand"]=sbar1.set

window.mainloop()