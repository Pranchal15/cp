


t=int(input())
for i in range(t):
    n = int(input())
    r = list(map(int,input().split()))[:n]
    r.reverse()
    for j in r:
        if j!=0:
            print(n-1-(r.index(j)))
            break

    