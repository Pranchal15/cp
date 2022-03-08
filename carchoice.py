t = int(input())
for i in range(0,t):
    x1,x2,y1,y2 = map(int,input().split())
    if (y1/x1) > (y2/x2):
        print(1)
    elif  (y1/x1) < (y2/x2):
        print(-1)
    else:
        print(0)