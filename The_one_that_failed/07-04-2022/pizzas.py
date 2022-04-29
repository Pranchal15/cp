import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    ans=math.ceil(n/k)
    print(int(ans))