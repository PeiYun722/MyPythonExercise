from bokeh.plotting import figure,show
import numpy as np

x=np.arange(10)
y=np.random.randint(1,10,10)#1~9產生10個隨機數

p=figure()

p.circle(x,y,size=25,color="#000079")#散點大小15

show(p)

