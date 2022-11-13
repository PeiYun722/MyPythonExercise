import numpy as np
import time

x=np.random.rand(1,10000)
y=list(x)

stat_time=time.time()
for i in x:
    sum1=np.sum(x)
    print(sum1)
    print("總共花%f秒"%(time.time()-stat_time))
    
stat_time=time.time()
for i in range(len(y)):
    sum2=sum(y)
    print(sum2)
    print("總共花%f秒"%(time.time()-stat_time))