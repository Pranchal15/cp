t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a= list(map(int,input().split()))[:n]
    a.sort()
    temp=a[0]
    flav=1
    for j in a:
        if j == temp:
            continue
        else :
            flav+=1
            temp =j
    if n-flav>=x:
        print(flav)
        continue
    else :
        print(n-x)
        continue
