liczba = int(input("wybierz liczbe "))
def renż(x, y):
    if liczba in range(x, y):
        result = ("tak")
    else:
        result = ("nie")
    return result
rezultat = renż(2, 15)
print(rezultat)

    

