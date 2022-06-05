t=int(input())
for i in range(0,t):
    n = int(input())
    l = list(map(int,input().split()))[:n]
    max =l[0]+l[len(l)-1]
    for i in range(len(l)-1):
        if l[i]+l[i+1]>=max:
            max = l[i]+l[i+1]
    print(max)
