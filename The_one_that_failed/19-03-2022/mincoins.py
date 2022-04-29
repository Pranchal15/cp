t = int(input())
for i in range(t):
    coins=0
    x = int(input())
    if x%5!=0:
        print(-1)
    else:
        coins = (int((x/10)))+ int((x%10)/5)
        print(coins)