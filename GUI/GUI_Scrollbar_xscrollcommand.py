import tkinter as tk
window=tk.Tk()
song="Cause I-I-I'm in the stars tonight,\
So watch me bring the fire and set the night alight (hey)\
Shining through the city with a little funk and soul\
So I'ma light it up like dynamite, whoa oh oh"
sbar1=tk.Scrollbar(window,orient=tk.HORIZONTAL)
txt1=tk.Text(window,width=40,height=10,wrap=tk.NONE)
txt1.insert(tk.END,"dynamite\n")
txt1.insert(tk.END,song)
sbar1.pack(side=tk.BOTTOM,fill=tk.X)
txt1.pack(side=tk.LEFT,fill=tk.Y)
sbar1["command"]=txt1.xview
txt1["xscrollcommand"]=sbar1.set
window.mainloop()
