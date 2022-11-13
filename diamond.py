
"列印菱形"

while(True):
    num=input("請輸入層數(奇數):")
    if num.isdigit()==True:
        num=int(num)
        if num%2==1:
            break
        else:
            print("輸入不為奇數!")
    else:
        print("輸入不為正整數!")
    
for i in range(-(num//2),num//2+1):
    print(" "*abs(i),end="")
    for j in range(0,num-2*abs(i)):
        print("*",end="")
    print()
    