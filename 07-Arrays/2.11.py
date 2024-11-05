temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7]
NOM = len(temperatures)
print("Month: March")
print(f"number of measurements is {NOM}")
AT = sum(temperatures) / NOM
print(f"average temperature is {AT}")
print(f"minimum is {min(temperatures)}")
print(f"maximum is {max(temperatures)}")
i = 0
FD = 0
while i < NOM:
    if temperatures[i] < 0:
        FD += 1
    i += 1    
print(f"number of days with negative temp {FD}")
