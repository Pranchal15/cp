t = int(input())
while t :
    x,y=map(int,input().split())
    str1 = input()
    str2 = input()
    flag=0
    arr1 = [0]*100
    arr2 = [0]*100
    for i in range(x):
        arr1[ord(str1[i])]+=1
    for j in range(y):
        arr2[ord(str2[j])]+=1
    print(arr1)
    print(arr2)
    for k in range(65,90):
        if arr1[k]>arr2[k]:
            flag=1
        if flag:
            print("NO")
            break
    if flag==0:
        print("YES") 
        



