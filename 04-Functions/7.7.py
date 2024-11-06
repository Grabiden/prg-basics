<<<<<<< HEAD
def amount_to_pay(a):
    IP = a//5
    ID = (a - IP*5)//2
    IJ = a - ID*2 - IP*5
    result = (f"masz {IP}, {ID}, {IJ}")
    return result
fiut = amount_to_pay(23)
print(fiut)
    
=======
def binary_number(a):
    p = set(a)
    s = {"1", "0"}
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")

result = binary_number("101201")
print(result)        
>>>>>>> 09c1658965dd5dc9b1b8ffbc984b238fd3bd9459
