t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    a.sort()
    max = a[-1]
    count=0
    temp = a[0]
    j=1
    while j<n-1:
        if a[j]==temp:
            a[j]+=max
            max = a[j]
            count+=1
            j+=1
        else:
            temp = a[j]
            j+=1
    # for j in range(n-1):
    #     if a[j]==a[j+1]:
    #             a[j+1]+=max
    #             max = a[j+1]
    #             count+=1
    print(count)