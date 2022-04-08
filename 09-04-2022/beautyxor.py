t = int(input())
for i in range(t):
    n = int(input())
    b=1
    for j in range(2,n+1,2):
        b = b^j
        if j+1 < n+1:
            b=b&(j+1)
    print(b)
