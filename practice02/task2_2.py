def f22(x):
    a = (x & 0xff) << 8
    b = (x & 0x100) << 9
    c = (x & 0xe00) >> 7
    d = (x & 0x1fff000) << 7
    e = (x & 0xe000000) >> 20
    f = (x & 0x10000000) >> 10
    g = (x & 0x60000000) >> 29
    h = (x & 0x80000000) >> 15

    return hex(a + b + c + d + e + f + g + h)

print(f22(0x25d6d163))

print(f22(0x7cf2ffab))