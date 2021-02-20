from math import sin, cos, tan, pow

def f12(x):
    if x < 151:
        f = cos(sin(85*pow(x, 7))) - 49*pow(x,6)
    elif x < 178:
        f = x - 18*pow(x, 8)
    elif x < 277:
        f = 30*pow(x,6) + tan(x)
    else:
        f = pow((pow(x, 7) * 11 - x), 3) - 12 * pow(x,5)
    return "{:.2e}".format(f)
    
print(f12(258))
print(f12(142))