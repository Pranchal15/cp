n= input()
n= int(n)
if 1<=n<=100:
    i=0
    xi=0
    yi=0
    zi=0
    for i in range (0,n):
        x,y,z = input().split()
        x= int(x)
        y= int(y)
        z= int(z)
        if -100<=x<=100 and -100<=y<=100 and -100<=z<=100:
            xi=xi+x
            yi=yi+y
            zi=zi+z
        else : exit()
    if xi==0 and yi==0 and zi==0:
                print('YES')

    else : print('NO')
