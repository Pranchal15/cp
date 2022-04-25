t = int(input())
for i in range(t):
    list1 = list(map(int,input().split()))[:10]
    k = int(input())
    list1.reverse()
    for j in range(10):
        dif = list[j]-k
        if dif <0:
            print(10-j)
            break
        if dif ==0:
            if 

