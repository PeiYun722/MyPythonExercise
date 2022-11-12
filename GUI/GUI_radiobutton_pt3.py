import tkinter as tk
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("選項按鈕")
"""""""""""""""""
建立函式
    設定label元件顯示的文字text為字串加上fruit字典取出的選項
"""""""""""""""""
def shoMsg():
    lab_result["text"]="選項結果:"+var.get()

"""""""""""""""""
建立label
"""""""""""""""""
lab_title=tk.Label(window,text="請選擇最喜歡的水果:", width=30,bg="Gold").pack()
"""""""""""""""""
建立var，其類別為字串變數
"""""""""""""""""
var=tk.StringVar()
var.set("none") #設定var變數值為none(建立時沒有選項被選)
"""""""""""""""""
建立字典fruit,key:水果名稱,value:色彩值
"""""""""""""""""
fruit={"葡萄":"DarkViolet","蘋果":"LightCoral","奇異果":"LightGreen","芒果":"Orange"}
for tex,col in fruit.items():
    tk.Radiobutton(window,
                   text=tex,
                   value=tex,
                   variable=var,
                   bg=col,
                   width=20,
                   command=shoMsg).pack()
 
lab_result=tk.Label(window, width=30,bg="Pink")
lab_result.pack()
window.mainloop()