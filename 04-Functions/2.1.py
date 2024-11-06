import math
def trój(a, b, c):
    s = (a+b+c)/2
    pole = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return pole
pole1 = trój(3, 4, 5)
print(pole1)