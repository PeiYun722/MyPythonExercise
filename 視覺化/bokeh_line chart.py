from bokeh.plotting import figure,show

x=[i for i in range(5) ]
y=[0,1,4,9,16]
p=figure(plot_width=500,plot_height=500) #設定繪圖板高

#繪製折線圖
p.line(x,y,line_color="blue",legend_label="linear",line_dash="dashed")
 
show(p)