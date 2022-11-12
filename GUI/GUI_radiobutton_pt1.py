import tkinter as tk
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("選項按鈕")

"""""""""""""""""
printSelection函式:
    設定label元件的label1的顯示文字(text參數)
    為字串加上選項按鈕rb1點選的選項(以var變數透過get取得)
"""""""""""""""""
def printSelection():
   label1.config(text="您是"+var.get())
   
"""""""""""""""""
*建立var
"""""""""""""""""
var=tk.StringVar()#建立變數var,設定變數類別為字串變數
var.set("男生")#設定變數var的值為字串(男生),作為選項按鈕建立時的預設值
# var.set(0):讓預設值為空

"""""""""""""""""
建立最上方標籤
"""""""""""""""""
label1=tk.Label(window,text="尚未選擇",bg="darkorange",width=30)
label1.pack()

"""""""""""""""""
*建立radiobutton

    建立並布置男生的選項按鈕rb1
    text參數設定為字串(男生):為選項按鈕顯示的文字
    variable參數:設定目前選項按鈕的狀態，設定為var
    value參數:為此選項被點選時的值
    選項按鈕建立時男生被點選
    以command參數設定當選項被點選時要呼叫執行的函式 printSelect()
"""""""""""""""""
rb1=tk.Radiobutton(window,text="男生",
                   variable=var,
                   value="男生",
                   command=printSelection)
rb1.pack()
rb2=tk.Radiobutton(window,text="女生",
                   variable=var,
                   value="女生",
                   command=printSelection)
rb2.pack()


window.mainloop()
