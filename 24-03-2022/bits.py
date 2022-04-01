n=int(input())
print(n|0)
print(n>>1,2)
c=0

while(n):
    print(n,6)
    if n|0!=0:
        c=c+1 
        print(c,9)
    n>>=1 
    print(n,11)
print(c)