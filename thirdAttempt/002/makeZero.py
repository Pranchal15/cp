t = int(input())
for i in range(t):
    n=int(input())
    count=0

    r = list(map(int,input().split()))[:n]
    maxim = max(r)
    binary = len(bin(maxim).replace("0b",""))
    for j in range(0,binary):
        flag =0
        for k in r :
            if k!=0:
                if k^1==k-1:
                    count+=1
                    flag =1
            r[r.index(k)]=k>>1
            if flag:
                break
    print(count,"ans")
