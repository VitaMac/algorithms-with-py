import math

def okto_modulis(c) :
    c1, c2, c3, c4, c5, c6, c7, c8 = c
    m = math.sqrt(c1 ** 2 + c2 ** 2 + c3 ** 2 + c4 ** 2 + c5 ** 2 + c6 ** 2 + c7 ** 2 + c8 ** 2)
    return m

def okto_daugyba(d) :
    z1, z2, z3, z4, z5, z6, z7, z8 =d
    b1 = z1 * z1 - z2 * z2 - z3 * z3 - z4 * z4 - z5 * z5 - z6 * z6 - z7 * z7 - z8 * z8
    b2 = z2 * z1 + z1 * z2 - z4 * z3 + z3 * z4 - z6 * z5 + z5 * z6 + z8 * z7 - z7 * z8
    b3 = z3 * z1 + z4 * z2 + z1 * z3 - z2 * z4 - z7 * z5 - z8 * z6 + z5 * z7 + z6 * z8
    b4 = z4 * z1 - z3 * z2 + z2 * z3 + z1 * z4 - z8 * z5 + z7 * z6 - z6 * z7 + z5 * z8
    b5 = z5 * z1 + z6 * z2 + z7 * z3 + z8 * z4 + z1 * z5 - z2 * z6 - z3 * z7 - z4 * z8
    b6 = z6 * z1 - z5 * z2 + z8 * z3 - z7 * z4 + z2 * z5 + z1 * z6 + z4 * z7 - z3 * z8
    b7 = z7 * z1 - z8 * z2 - z5 * z3 + z6 * z4 + z3 * z5 - z4 * z6 + z1 * z7 + z2 * z8
    b8 = z8 * z1 + z7 * z2 - z6 * z3 - z5 * z4 + z4 * z5 + z3 * z6 - z2 * z7 + z1 * z8
    kva = [b1, b2, b3, b4, b5, b6, b7, b8]
    return kva

def okto_suma(g,r):
    g1, g2, g3, g4, g5, g6, g7, g8 = g
    r1, r2, r3, r4, r5, r6, r7, r8 = r
    suma = s1, s2, s3, s4, s5, s6, s7, s8 = [g1 + r1, g2 + r2, g3 + r3, g4 + r4, g5 + r5, g6 + r6, g7 + r7, g8 + r8]
    return suma

