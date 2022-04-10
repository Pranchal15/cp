t=int(input())
for _ in range(t):
    x=int(input())
    flag = 1
    if x%2!=0:
        print(-1)
    else:
        for j in range(0,31):
            b = 2**j
            a=0
            c=int(x/2)-(b)
            if ((a^b)+(b^c)+(c^a))==x and a!=b and b!=c and c!=a:
                print(a,b,c)
                flag =0
                break
        if flag ==1 :
            print(-1)

            
        