t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    lst=[0]*n
    for j in range(n):
        if s[j]=='1':
            lst[n-j-1]=j+1
    k=n-2
    while k>=0:
        lst[k]+=lst[k+1]
        k-=1
    ans =0
    bitpower =1
    for l in range(n):
        if lst[l]%2!=0:
            ans+=bitpower
            ans=ans%998244353 
        bitpower=(bitpower*2)%998244353 
    print(ans)




                 

