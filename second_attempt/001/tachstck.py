n,d = map(int,input().split())
l =[]
for i in range(n):
    x = int(input())
    l.append(x)
l.sort()
i=0
count =0
while i<n-1:
    if l[i+1]-l[i]<=d:
        count+=1
        i+=2
    else :
        i+=1
print(count)