T = int(input())
for i in range(T):
    count =0
    n = int(input())
    s =list(map(int, input().split()[:n]))
    for i in s:
        if i>=10 and i<=60 :
            count= count +1
    print(count)