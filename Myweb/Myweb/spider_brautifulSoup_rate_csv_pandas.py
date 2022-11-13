import pandas as pd
import csv

fn=r"C:\MyPython\Myweb\twrate.csv"
with open(fn,encoding="utf8") as csvfile:
    csvReader=csv.reader(csvfile)
    listReport=list(csvReader)
    
for row in listReport:
    while "-" in row:
        i=row.index("-")
        row[i]=0
time_period=listReport[0]
time_period=time_period[1:]

listReport=listReport[1:]
bank=[]
newReport=[]
for row in listReport:
    bank.append(row[0])
    newReport.append(row[1:])
df=pd.DataFrame(newReport,columns=time_period,index=bank)
print(df)
my_max=df.max()
print(my_max)
