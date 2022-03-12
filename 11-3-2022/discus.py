t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    max =a
    if max<b:
        max=b
    if max<c:
        max = c
    print(max)