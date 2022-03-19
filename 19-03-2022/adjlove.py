def func(a):
    even =0
    odd=0
    odds=[]
    evens=[]
    ans=[]
    for j in a:
        if j%2==0:
            even+=1
            evens.append(j)
        else:
            odd+=1
            odds.append(j)
    if odd >2:

        if odd%2==0:
            if len(odds)==0:
                print(-1)
            else:
                ans=ans+odds
                ans=ans+evens
                print(' '.join(map(str,ans)))
        else:
            if len(evens)==0:
                print(-1)
            else:
                last = odds[-1]
                odds.pop()
                ans = ans+odds
                ans = ans + evens
                ans.append(last)
                print(' '.join(map(str,ans)))
    else:
        print(-1)

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    func(a)
    
    