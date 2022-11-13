num=input("請輸入一正整數:")
if num.isdigit()== True:
    num=eval(num)
    if num%4==0 and num%7==0:
        print(num,"是4和7的倍數")
    elif num%4==0:
        print(num,"是4的倍數")
    elif num%7==0:
        print(num,"是7的倍數")
    else:
        print(num,"不是4和7的倍數")
else:
    print("不是正整數，請再輸入一次")