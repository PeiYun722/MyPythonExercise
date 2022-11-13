from bokeh.plotting import figure,show,output_file,save
#設定資料
x=0
y=0 
radius=1 #半徑
start_angle=[0,1.8,2.5,3.7,5.6]
end_angle=[1.8,2.5,3.7,5.6,0]
color=["#6F00D2","#B15BFF","#DCB5FF","#FAF4FF","#28004D"]

p=figure()
p.wedge(x,y,radius,start_angle,end_angle,color=color)
show(p)

output_file("pie_chart.html") #設定檔名
save(p) #儲存檔案
