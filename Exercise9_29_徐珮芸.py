"""
請讀取drugstore.csv檔案，並找尋在板橋區的藥局後，再寫入新檔案
"""
import csv
#讀取
fp=r"drugstore.csv"
with open(fp,encoding="utf8") as file:
    readfile=list(csv.reader(file))
#寫入
with open(r"new_drugstore.csv","w",newline="",encoding="utf8") as file:
    writefile=csv.writer(file)
    writefile.writerow(readfile[0])#寫入第一行
    for i in range(len(readfile)):
        if readfile[i][2]=="板橋區": #判斷地區是否為板橋區
            writefile.writerow(readfile[i])
    