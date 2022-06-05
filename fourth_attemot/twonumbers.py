t=int(input())
for i in range(0,t):
    x=int(input()) 
    if x%2==0:
        print(int(((x/2)+1)*((x/2)-1))-1)
    else :
        print(int((x/2)*(x-(x/2)))-1)
    
   