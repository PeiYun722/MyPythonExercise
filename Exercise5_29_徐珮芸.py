#身分證驗證
import re
checkID="ABCDEFGHJKLMNPQRSTUVXYWZIO"

#資料驗證
while(True):
    ID=input("請輸入身分證:") 
    ID=ID.upper() 
    regular=re.compile(r'[A-Z][1,2]\d{8}') 
    if re.fullmatch(regular,ID):
        break
    else:
        print("輸入資料不為「英文碼+9位數字」")
        
#計算加權 
firstID=ID[0] #取得使用者首位英文字
firstIDNum=10+checkID.find(firstID) #取得首位英文字(firstID)對應的數值
total=(firstIDNum//10)+(firstIDNum%10)*9 #計算首位英文字母加權值

for i in range(1,9):
    total+=int(ID[i])*(9-i) #計算至第8位加權值

total+=int(ID[9])   #計算至第9位加權值
#判斷加權後是否為10的倍數
if total%10==0:
    print("身份證字號正確")
else:
    print("身份證字號錯誤")