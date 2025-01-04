###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    n = 1
    for line in file:
        print(f"{n}. {line.strip()}")  
        n += 1
        
        