t=int(input())
for _ in range(t):
    x,y,m=map(int,input().split())
    if x*m < y:
        print('yes')
    else:
        print('no')