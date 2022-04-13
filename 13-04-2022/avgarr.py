t = int(input())
def sumofconsec(n):
    return (n*(n+1))/2

for i in range(t):
    n,x = map(int,input().split())
    arr = []
    if n ==1 :
        print(x)
        continue
    if n ==2:
        print(0,2*x)
        continue
    # wanted = n*x
    # sum = sumofconsec(n-1)
    # remaining = int(wanted - sum)
    # if not (remaining<n):
    #     for i in range(1,n):
    #         arr.append(str(i))
    #     arr.append(str(remaining))
    #     print(' '.join(arr))
    #     continue
    if n%2==0:
        l=1
        for pr in range(0,int(n/2)-1):
            if(l!=(n*x)) and l>(-1000):
                arr.append(str(-1*(l)))
            l+=1
        l=1
        arr.append('0')
        for ku in range(int(n/2),n-1):
            if(l!=(n*x)):
                arr.append(str(l))
            l+=1
        arr.append(str(n*x))
        print(' '.join((arr)))
        continue
    else :
        l=1
        for pr in range(0,int(n/2)):
            if(l!=(n*x)):
                arr.append(str(-1*(l)))
            l+=1
        arr.append(str(n*x))
        l=1
        for ku in range(int(n/2)+1,n):
            if(l!=(n*x)):
                arr.append(str(l))
            l+=1
        print(' '.join((arr)))
        continue
sum =0
for kunal in arr:
    sum = sum +int(kunal)
print(sum/n)



