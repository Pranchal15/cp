T = int(input())
for i in range (T):
    x,a,b=input().split()
    if ((int(a)*1)+(int(b)*2) >= int(x)):
        print('Qualify')
    else:
        print('NotQualify')
