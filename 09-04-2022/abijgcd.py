import math
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    flag =0
    if a%2==0:
        if a+2<=b:
            print(a,a+2)
            flag=1
    else :
        if a%3==0:
                
            if a+3<=b:
                print(a,a+3)
                flag=1
        else :
            if a+3<=b:
                print(a+1,a+3)
                flag=1
    if flag ==0:
        print(-1)