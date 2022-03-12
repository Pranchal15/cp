t = int(input())
for i in range(t):
    a=input()
    n =len(a)
    k=1
    count=0
    max=0
    while k<n:
        if a[k] is a[0] or a[k] is a[n-1]:        
            if max<count:
                max=count
            count =0
            k+=1
        else:
            count +=1
            k+=1
    if max==0:
        print(-1)
    else:
        print(max)


