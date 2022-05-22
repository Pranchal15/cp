
t=int(input())
for i in range(t):
    n = int(input())
    # r = list(map(int,input().split()))[:n]
    r=input()
    j=0
    p=n-1
    count=0
    while j<p:
        # print(r[j],r[n-j-1],j)
        if (r[j]!=r[p]):
            count +=1
        j+=1
        p-=1
    if count%2==0:
        print(int(count/2))
    else :
        print(int(count/2)+1)