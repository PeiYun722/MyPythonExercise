import tkinter as tk

"""""""""""""""""
方法:
建立空串列selection儲存勾選的核取按鈕要存入的字串
#設定顯示勾選結果的Label(result)的內容為字串加上串列seletion的內容
->條件式:
    判斷條件:第一個核取按鈕取得的值是否為true(已核取)
            若條件成立，執行:將字串Java放入串列selection中
"""""""""""""""""
def show_sel():
    selection=[] #建立空串列(List)
    if var1.get()==True: #取得值
        selection.append("Java") #將"Java"字串加入selection串列最後
    if var2.get()==True:
        selection.append("Python")
    if var3.get()==True:
        selection.append("C++")
        
    result["text"]="選取結果:"+",".join(selection)#join():以指定的字符連接生成一个新的字串
    #result.config(text="選取結果:"+",".join(selection))
    #result:即為label元件的text參數，設定方式為 label元件名["text"]=文字內容
    
"""""""""""""""""
建立視窗
"""""""""""""""""
window=tk.Tk()
window.title("Checkbutton元件")

"""""""""""""""""
建立最上方標籤
"""""""""""""""""
tk.Label(window,text="程式語言:",width=30,background="cyan").pack()

"""""""""""""""""
建立變數var1,設定變數類別為布林變數
設定變數var1的值為0(False),表示核取按鈕未勾選
此時var1,2,3為單純變數，尚未與核取按鈕連結
"""""""""""""""""
var1=tk.BooleanVar()
var1.set(0)#如果為1，則啟動程式時預設打勾,預設為false(0)
var2=tk.BooleanVar()
var2.set(0)
var3=tk.BooleanVar()
var3.set(0)

"""""""""""""""""
建立並布置核取按鈕tk.checkbutton(.....)
以variable參數設定核取按鈕目前的狀態，設定為var1，
則核取按鈕建立時未勾選狀態.
並以command參數設定當核取按鈕點擊時要呼叫執行函式(show_sel)
"""""""""""""""""
tk.Checkbutton(window,text="Java",variable=var1,command=show_sel).pack()
tk.Checkbutton(window,text="Python",variable=var2,command=show_sel).pack()
tk.Checkbutton(window,text="C++",variable=var3,command=show_sel).pack()
"""""""""""""""""
建立顯示標籤
"""""""""""""""""
result=tk.Label(window,text="選取結果:",width=30,background="darkorange")
result.pack() #pack不能放在上列

window.mainloop()