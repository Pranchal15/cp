t = int(input())
for i in range(t):
    s1=input()
    s2=input()
    answer=''
    n=0
    while n<5:
        if s1[n]==s2[n]:
            answer = answer +'G'
        else :
            answer = answer+'B'
        n+=1
    print(answer)