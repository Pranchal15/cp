t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    
    if y%2==0 and (x-y)%2==0:
        print('YES')
    elif y%2!=0 and (x-y)%2!=0:
        print("Yes")
    else : print('NO')