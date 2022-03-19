t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if n%3==0:
        cost = int(n/3) * 2 *x
    else:
        cost = (int(n/3)*2*x)+((n%3)*x)
    print(cost)