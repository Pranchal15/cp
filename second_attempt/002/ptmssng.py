t=int(input())
for i in range(t):
    n = int(input())
    num = (4*n)-1
    x=[]
    y=[]
    nfx=0
    nfy=0
    for j in range(num):
        x1,y1=map(int,input().split())
        x.append(x1)
        y.append(y1)
    x.sort()
    y.sort()
    k=0
    while k<num-1:
            if x[k]==x[k+1]:
                k+=2
                continue
            else :
                nfx=x[k]
                break
    else :
        nfx=x[k+1]
    k=0
    while k<num:
            if y[k]==y[k+1]:
                k+=2
                continue
            else :
                nfy=y[k]
                break

    else :
        nfy=x[k+1]

    print(nfx,nfy)

