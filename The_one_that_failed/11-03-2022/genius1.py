t= int(input())
for i in range(t):
    n,x = map(int,input().split())
    if x==0:
        if n>=4:
            correct = 1 
            incorrect = 3
            unat=n-correct-incorrect
            if correct+incorrect+unat ==n and correct>=0 and incorrect>=0 and unat >=0:
                print('YES')
                print(correct,incorrect,unat)
            else:
                print('NO')
        else:
            print('YES')
            print(0,0,n)
    elif x==1:
        if n>=3:
            correct =1
            incorrect =2
            unat=n-3
            if correct+incorrect+unat ==n and correct>=0 and incorrect>=0 and unat >=0:
                print('YES')
                print(correct,incorrect,unat)
            else:
                print('NO')
        else:
            print('NO')
    elif x%3==2:
        if n>=2:
            correct = int((x+1)/3)
            incorrect = 1
            unat = n-correct-incorrect
            if correct+incorrect+unat ==n and correct>=0 and incorrect>=0 and unat >=0:
                print('YES')
                print(correct,incorrect,unat)
            else:
                print('NO')
        else:
            print('NO')
    elif x%3==1:
        if n>=3:
            correct = int((x+2)/3)
            incorrect=2
            unat = n-correct-incorrect
            if correct+incorrect+unat ==n and correct>=0 and incorrect>=0 and unat >=0:
                print('YES')
                print(correct,incorrect,unat)
            else:
                print('NO')
        else:
            print('NO')
    elif x%3==0:
        if n>=1:
            correct = int(x/3)
            incorrect=0
            unat = n-correct
            if correct+incorrect+unat ==n and correct>=0 and incorrect>=0 and unat >=0:
                print('YES')
                print(correct,incorrect,unat)
            else:
                print('NO')
    else :print('NO')
