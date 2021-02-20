from math import modf, exp

def f13(n, m):
    f = 0
    for i in range(1, n + 1):
        f+= 99 * pow(i, 7) + pow(i, 5)
        for j in range(1, m + 1):
            f+= j - exp(i)

    return "{:.2e}".format(f)
print(f13(25, 35))
print(f13(26, 28))
            