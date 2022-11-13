# 請撰寫一程式，請使用者輸入容器大小n，
# 然後在該慶中產生n個1~100的亂數
# 以list、tuple、set以及dict的方式輸出
import random

while True:
    times=input("請輸入容器大小:")
    if times.isdigit():
        times=int(times)
        break
    else:
        print("輸入不為正整數!")

#建立容器
set1=set(random.sample(range(1,100),times))
list1=list(set1)
tuple1=tuple(set1)
key=[i for i in range(1,times+1)]
dict1=dict(zip(key,list1))
    
print(set1)
print(list1)    
print(tuple1)
print(dict1)

    
    