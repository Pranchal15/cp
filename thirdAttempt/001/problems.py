arr= list(map(int,input().split()))[:4]
count=0
for i in arr :
    if i>=10:
        count +=1
print(count)
    