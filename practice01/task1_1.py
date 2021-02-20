from math import sin, log, exp, pow
def f11(x):
    f = (94*pow(x, 3) + 75*pow(x, 6))/(sin(2*pow(x,3))+log(x)) - (log(x) - pow(x, 2) - 75)/(x*x - log(x)) - (6*x*x + exp(x))/(exp(x) + pow(x, 6))
    return "{:.2e}".format(f)
print(f11(12))
print(f11(43))
