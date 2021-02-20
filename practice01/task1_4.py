
from math import cos
def f14(n):
    if n == 0:
        return 4
    else:
        return 1/51*f14(n - 1) + cos(f14(n-1)) - 69 

print(f14(8))
print(f14(6))
