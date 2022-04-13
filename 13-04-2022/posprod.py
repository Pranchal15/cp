t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()[:n]))
    pos = 0 
    neg=0
    for j in a :
        if j > 0:
            pos+=1
        if j <0:
            neg+=1

    ans = int((pos*(pos-1))/2)+ int((neg*(neg-1))/2)
    print(ans)