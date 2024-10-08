a = int(input("długość krawędzi 1?"))
b = int(input("długość krawędzi 2?"))
c = int(input("długość krawędzi 3?"))
volume = a * b * c
surface_area = a * b * 2 + b * c * 2 + c * a * 2
print(f"objętość to {volume}")
print(f"pole powierzchni to {surface_area}")