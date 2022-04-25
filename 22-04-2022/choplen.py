
n,d = map(int,input().split())
arr =[]
count =0
for j in range(n):
    s=int(input())
    arr.append(s)
arr.sort()
for k in range(0,n,2):
    print(k)
    if k <n-1:
        if abs(arr[k]-arr[k+1])<=d:
            count +=1

print(count)

