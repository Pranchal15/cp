t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    if x<=y and y<=x+200:
        print('YES')
    else :print("NO")