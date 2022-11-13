x=input("請輸入一個字元:")
if x.isalpha():
    print(x,"是英文字母")
elif x.isdigit():
    print(x,"是數值")
else:
    print(x,"是其他字元")