def gsd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def simplify_fraction(fraction):
    d = gsd(fraction[0], fraction[1])
    return (fraction[0] / d, fraction[1] / d)