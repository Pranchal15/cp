def func(x):
    if x%2==0:
        x=int(x/10)
        while x>0:
            temp = x%10
            if (temp)%2==0:
                return True
            x=int(x/10)
    else :
        x=int(x/10)
        while x>0:
            temp = x%10
            if temp%2!=0:
                return True
            x=int(x/10)
    return False

t=int(input())
for i in range(t):
    x = int(input())
    if func(x):
        print("YES")
    else:
        print('NO')
    