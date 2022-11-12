import tkinter as tk
"""""""""""""""""
建立printSelection
  ->以cities字典，透過var變數的get()方法，
    取得選項按鈕所選的程式
"""""""""""""""""
def printSelection():
    print(cities[var.get()])
    
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("選項按鈕")

"""""""""""""""""
建立var設定var變數為整數變數
"""""""""""""""""
var=tk.IntVar()
var.set(0)

"""""""""""""""""
建立標籤
"""""""""""""""""
label1=tk.Label(window,text="選擇最喜歡的城市",
                fg="blue",
                bg="darkorange",
                width=30).pack()

"""""""""""""""""
*迭代:變數歷遍一集合物件中的所有項目
     變數逐一被設定到一集合物件中之所有項目
    (自動) 通常用迴圈

*建立迴圈變數val,city依序對應設定到字典cities以items()方法取出的key,value，
以val,city建立選項按鈕，
city設定到選項文字(text)，
val設定到選項按鈕的值，
var設定當建立選項的目前狀態(variable)，整數為個選項項目
"""""""""""""""""
cities={0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"台北"}#以字典建立程式的選項
for val,city in cities.items(): #dict.item*():返回key,value(ex.0,"東京")
    tk.Radiobutton(window,text=city,
                   variable=var,
                   value=val,
                   command=printSelection).pack()
    
    
window.mainloop()