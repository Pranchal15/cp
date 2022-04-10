t = int(input())
for i in range(t):
    n = int(input())
    rem = n%4
    if rem ==0:
        print(n+3)
        continue
    elif rem ==1:
        print(n)
        continue
    elif rem==2 or rem ==3:
        print(3)
        continue
    