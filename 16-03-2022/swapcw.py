def func(s):
    arr=list(s)
    sortedArr=list(s)
    sortedArr.sort()
    j=0
    flag = 0
    while j<n:
        if arr[n-j-1] is sortedArr[j] or arr[j] is sortedArr[j]:
            j+=1
        else: return False
    return True


t=int(input())
for i in range(t):
    n = int(input())
    s = input()
    if func(s):
        print('YES')
    else: print('NO')
    
            
    