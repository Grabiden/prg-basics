<<<<<<< HEAD
def counter(string,letter):
    count = string.count(letter)
    return count
result = counter("You never get a second chance to make a first impression","e")
print(result)
=======
#funkcyja
miesiące = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
def month(a):
    result = miesiące[a] 
    return result
    

b = int(input("numer miesiąca ")) - 1
wynik = month(b) 


#koniec kodu6
print(f"the name of month {b+1} is {wynik}")
>>>>>>> 09c1658965dd5dc9b1b8ffbc984b238fd3bd9459
