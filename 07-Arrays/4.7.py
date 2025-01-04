imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
listy = []
for imie in imiona:
    listy.append(list(imie))

print(listy) 
liczby = []
for n in listy:
    liczby.append(len(n))

print(liczby)
print(max(liczby))