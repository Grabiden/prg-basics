#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN

cena = int(input("ile żeś stoł "))

if cena > 6:
 print("koszt to 20 PLN")
elif cena >= 3:
 print("koszt to 15 PLN")
elif cena >= 1:
 print("koszt to 5 PLN")
else:
 print("darmo")
     