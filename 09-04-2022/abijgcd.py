import math
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    j=a+1
    while j<=b:
        if math.gcd(a,j)>1:
            print(a,j)
            break
        j+=1
    else:
        print(-1)