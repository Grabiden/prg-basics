###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
<<<<<<< HEAD
    n = 1
    for line in file:
        print(f"{n}. {line.strip()}")  
        n += 1
        
        
=======
    count = 0
    for line in file:
        count += 1
        print(f"{count}.{line}", end="")
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
