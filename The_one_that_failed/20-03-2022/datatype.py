t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if x<=n:
        print(x)
    else:
        print(x%(n+1))