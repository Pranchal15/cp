t = int(input())
for i in range(t):
    a = list(map(int,input().split()))[:10]
    k = int(input())
    deleted =0
    last = 10
    a.reverse()
    for i in range(10):
        deleted +=a[i]
        if deleted<k:
            continue
        elif deleted > k:
            print(10-i)
            break
        elif deleted==k:
            last = i
            while a[last+1]==0 and last+1<10:
                        last+=1
            print(10-last-1)
            break
    
            

        


