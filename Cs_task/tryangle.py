t=int(input())
for i in range(t):
    h= int(input())
    for i in range(h):
        for j in range(h):
            if j==0:
                print("*",end=" ")
            elif i==j:
                print("*",end=" ")
            elif i==h-1:
                print("*",end=" ")
            else :
                print(" ")
    print("\n")
