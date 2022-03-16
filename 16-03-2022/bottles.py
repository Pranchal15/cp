t = int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    ans = int(k/x)
    if ans>n:
        print(n)
    else:
        print(ans)