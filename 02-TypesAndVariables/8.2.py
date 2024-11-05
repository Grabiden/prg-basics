###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

x = int(input("wprowadź temperature C "))
K = x + 273.15
F = (x * 9/5) + 32
print(f"temperatura w kelvinach {K}")
print(f"temperatura w fahrenheitach {F}")
print(f"temperatura w celcjusza {x}")
