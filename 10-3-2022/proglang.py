t=int(input())
for i in range(t):
    a,b,a1,b1,a2,b2=map(int,input().split())
    if a==a1 or a==b1:
        if b==a1 or b==b1:
            print(1)
    elif a==a2 or a==b2:
        if b==a2 or b==b2:
            print(2)
    else:
        print(0)