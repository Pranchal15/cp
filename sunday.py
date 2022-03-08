t = int(input())
for i in range(t):
    n = int(input())
    hol = n+8
    s = list(map(int,input().split()))[:n]
    for i in s:
        if i%7==0 or i%7 ==6:
            hol = hol -1 
    print(hol)