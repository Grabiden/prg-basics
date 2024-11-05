def amount_to_pay(a):
    IP = a//5
    ID = (a - IP*5)//2
    IJ = a - ID*2 - IP*5
    result = (f"masz {IP}, {ID}, {IJ}")
    return result
fiut = amount_to_pay(23)
print(fiut)
    