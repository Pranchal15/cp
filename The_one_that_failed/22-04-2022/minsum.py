t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    a.sort()
    print(a[0]+a[1])