a,b,c=map(int,input().split())
print((a^b)+(b^c)+(a^c))
# a,b=map(int,input().split())
# print(a^b)
# for k in range(0,(100),2):

#     for i in range(0,100):
#         for j in range(0,100):
#             if (i^j)+i+j==k:
#                 print(i,j,k)
# else :print('no')
# for x in range(2,2**10,2):
#     print(x,end=' ')
#     a = 0
#     flag1 = 0
#     flag2 = 1
#     for b in range(1,2**10):
#         for c in range(1,2**10):
#             if (b^c)+b+c == x and b!=c!=a:
#                 flag1 = 1
#                 flag2 = 0
#                 print(a,b,c)
#                 break
#         if flag1 == 1:
#             break
#     if flag2 == 1:
#         print("NOPE")