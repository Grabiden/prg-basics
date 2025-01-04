with  open('pets.txt', 'r') as file:
    contener = file.read()
contener_dwa = contener.split()
dziub = len(contener_dwa)
print(dziub)