###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
<<<<<<< HEAD
with open(employees_file, 'r') as empleyees:
   with open(position_file, 'w') as output:
      for line in empleyees:
         if job_title in line:
            output.write(line)
=======
with open('it_company.csv', 'r') as file:
   with open('pp', 'w') as file:
      for line in file:
         if job_title in file:
            content = file.write()
>>>>>>> 11cd2cebed6eda48bd3f9bc9be5b72ae7019f7cf
