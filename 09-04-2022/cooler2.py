import math
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    ans =int(y/x)
    if y%x==0 :
        print(ans-1)
    else :
        print(ans)