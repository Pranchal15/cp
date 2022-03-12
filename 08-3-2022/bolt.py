T = int(input())
solutions = []
if (1 <= T <= 100000):
    for x in range(T):
        k1, k2, k3, v = (input().split())
        k1 = float(k1)
        k2 = float(k2)
        k3 = float(k3)
        v = float(v)
        time = round(100/(k1*k2*k3*v), 2)
        if time < 9.58:
            solutions.append('YES')
        else:
            solutions.append('NO')
for i in solutions:
    print(i)
