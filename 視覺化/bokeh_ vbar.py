from bokeh.plotting import figure,show
import numpy as np

x=np.arange(10)
y=np.random.randint(1,11,10)#1~10產生10個隨機數

p=figure()

p.vbar(x, top=y, width=0.5,bottom=0,color="#FF79BC")

show(p)
