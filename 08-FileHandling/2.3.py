###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
<<<<<<< HEAD
with open(original_file, 'r') as file:
   content = file.read()



# write the content to the target file (copy)
with open(target_file, 'w') as file:
   file.write(content)
=======
with open('healthy_lifestyle.txt', 'r') as file:
   content = file.read()
...
...

# write the content to the target file (copy)
with open('copy_healthy_lifestyle.txt', 'w') as file:
    result = file.write(content)
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
