def occurs(number, array):
    if number in array:
        return True
    else:
        return False


numbers = int(input("Wprowadź liczbe "))
arr = [15, 38, 7, 23, 14]
if occurs(numbers, arr) == True:
    print("liczba znajduje sie w liście")
else:
    print("liczba nie znajduje sie w liście")