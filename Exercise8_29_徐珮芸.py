"""
請撰寫一程式，讀取data.txt內容，並將檔案內的數字加總後輸出，
總加結果為610
"""
#讀取
with open(r"read.txt") as file:
    row =file.readline() 
list1=row.split( )#將字串分割，輸出成list
int_list1=map(int,list1) #str轉型成int
print(sum(int_list1))