T = input()
T = int(T)
solutions = []
for i in range(T):
    N = int(input())
    if N > 4:
        num_layers = int(N/4)
        n = int(N % 4)
        min = (num_layers * 44)+16
        if n == 1:
            max = (min-(n*4)+20)
        if n == 2:
            max = (min-(n*4)+36)
        if n == 3:
            max = (min-(n*4)+51)
        if n == 0:
            max = min
    if N <= 4:
        if N == 1:
            max = 20
        if N == 2:
            max = 36
        if N == 3:
            max = 51
        if N == 4:
            max = 60
    solutions.append(max)


for i in solutions:
    print(i)
