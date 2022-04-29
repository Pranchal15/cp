t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    b = list(map(int,input().split()))[:n]
    a.sort()
    flag=0
    j=0
    while j<n:
        if a[j]==b[j]:
            j+=1
        else :
            flag =1
            break
    if flag ==1:
        print('no')
    else:
        print('yes')
 