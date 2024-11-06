<<<<<<< HEAD
chuj = input("wpisz numer karty kredytowej ")
result = chuj[:2] + 8*"*" + chuj[12:]
print(result)
=======
liczba = int(input("wybierz liczbe "))
def renż(x, y):
    if liczba in range(x, y):
        result = ("tak")
    else:
        result = ("nie")
    return result
rezultat = renż(2, 15)
print(rezultat)

    

>>>>>>> 09c1658965dd5dc9b1b8ffbc984b238fd3bd9459
