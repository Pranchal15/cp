t = int(input())
for k in range(t):
    n = int(input())
    s = input()
    time = 0
    i=0
    while i < n:
        j=i
        while j<n and s[j]==s[i]:
            j+=1
        time += (j-i+1)//2
        i=j
        
    print(time)