t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    div = int(x/3)
    if x%3==0 and div<=n:
        if x==0 and n>=4:
            correct = 1 
            incorrect = 3
            unat=n-correct-incorrect
            print('YES')
            print(correct,incorrect,unat)
        elif x==0 and n<4:
            print('NO')
        else:
            correct = div
            incorrect=0
            unat = 0
            print('YES')
            print(correct,incorrect,unat)
    elif x%3==1 and (div)+3<=n:
        correct = div+1
        incorrect =2
        unat=n-correct-incorrect
        print('YES')
        print(correct,incorrect,unat)
    elif x%3==2 and div+2<=n:
        correct=div+1
        incorrect=1
        unat=n-correct-incorrect
        print('YES')
        print(correct,incorrect,unat)
    else : print('NO')
    