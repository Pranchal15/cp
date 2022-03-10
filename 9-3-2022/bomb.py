t = int(input())
for i in range(t):
    count=0
    n,x=map(int,input().split())
    a = list(map(int,input().strip().split()))[:n]
    for j in range(n):
        if a[j]<x :
            count = j+1
    print(count)