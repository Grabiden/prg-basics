<<<<<<< HEAD
###
=======
##
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'
<<<<<<< HEAD

# Sort data alphabetically
seven_wonders.sort()
=======
seven_wonders.sort()
# Sort data alphabetically

>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf

# Write data to the file
with open(file_name, 'w') as file:
    for item in seven_wonders:
<<<<<<< HEAD
        file.write(item + '\n')
=======
        file.write(f'{item}\n')
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
