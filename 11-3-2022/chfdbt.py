def fun(n):
    if n==1 or n==2:
        return 1
    else:
        if n%2==0:
            return int(n/2)
        else :
            return int(n/2)+1    
t=int(input())
for i in range(t):
    n = int(input())
    answer = fun(n)
    print(answer)