t = int(input())
for _ in range(t):
    answer =''
    n,k= map(int,input().split())
    remaining = k
    s = list(map(int,input().split()))[:n]
    for i in range(n):
        if remaining>=s[i]:
            remaining = remaining - s[i]
            answer =answer+'1'

        else:
          answer=answer+'0'
    print(answer)