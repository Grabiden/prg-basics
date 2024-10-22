#funkcyja
miesiące = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
def month(a):
    result = miesiące[a] 
    return result
    

b = int(input("numer miesiąca ")) - 1
wynik = month(b) 


#koniec kodu6
print(f"the name of month {b+1} is {wynik}")