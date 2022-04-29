t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if k ==1 and n%4 ==0:
        print('on')
        continue
    if k ==0 :
        if n%4!=0:
            print('on')
            continue
        else:
            print('off')
            continue
    print('ambiguous')    