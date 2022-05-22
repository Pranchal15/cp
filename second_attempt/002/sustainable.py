def Possibility (N, M, A):
    count =0
    # Write your code here
    if N<3:
        if A[0]<A[1]:
            return 1
        else :
            return 0
    if N==3 and M==0:
        if A[0]<A[1] and A[1]<A[2]:
            return 1
        else :
            return 0
    elif N==3 and M>0:
        return 1
    for i in range(0,len(A)-2):
        if len(A)>2:

            try:
                if A[i]>A[i+1]:
                    A[i+1]=A[i+1]+A[i+2]+A[i+3]
                    A.pop(i+3)
                    A.pop(i+2)
                    count +=1
            except:
                A[-1]=A[-1]+A[-2]+A[-3]
                A.pop(-1)
                A.pop(-2)
                count +=1
                #  if A[i]>A[i+1]:
                #     A[i+1]=A[i+1]+A[i+2]+A[i+3]
                #     A.pop(i+2)
                #     A.pop(i+3)
                #     print(A)
                #     count +=1
            print(A)
            print(i)
        else :
            break
    Possibility(len(A),M,A)
    if count <=M:
        return 1
    else: return 0


T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))

    out_ = Possibility(N, M, A)
    print (out_,'ans')