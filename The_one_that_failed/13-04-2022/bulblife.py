t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    s =list(map(int, input().split()[:n-1]))
    sum=0
    for j in s:
        sum = sum + j
    if n*x > sum:

     print((n*x)-sum)
    else:
        print(0)
