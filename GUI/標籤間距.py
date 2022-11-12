"""""""""
設標籤間距:pady
"""""""""
import tkinter as tk
window=tk.Tk()
window.title("Label元件位置設定")
label1=tk.Label(window, text = "文字標籤一",
                width=15,
                bg="lightyellow")
label2=tk.Label(window, text = "文字標籤二",
                width=15,
                bg="lightblue")
label3=tk.Label(window, text = "文字標籤三",
                width=15,
                bg="lightgray")

"""""""""""""""
資料橫排，中間間隔10。side設定排版，RIGHT從右開始排
"""""""""""""""
# label1.pack(side=tk.RIGHT)
# label2.pack(side=tk.RIGHT,padx=10)
# label3.pack(side=tk.RIGHT)

"""""""""""""""
資料直排，中間間隔10。BOTTOM從底部開始(預設為TOP)
"""""""""""""""
label1.pack(side=tk.BOTTOM)
label2.pack(side=tk.BOTTOM,pady=10)
label3.pack(side=tk.BOTTOM)

window.mainloop()



