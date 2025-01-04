def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()
<<<<<<< HEAD
print(file_content)
print(file_lines)
# calculates the total number of cars parked

total = 0
for line in file_lines:
   total += int(line)
=======

# calculates the total number of cars parked
total = 0
for line in file_lines:
   srak = int(line)
   total += srak
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf

print('Total cars parked:', total)