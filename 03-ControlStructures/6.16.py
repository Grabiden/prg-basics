###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
extra_time = 0
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')


if extra_rinse == "y":
    extra_rinse = True
else:
    extra_rinse = False
if extra_spin == "y":
    extra_spin = True
else:
    extra_spin = False

if extra_rinse == True:
    extra_time += 15
else:
    extra_time += 0
if extra_spin == True:
    extra_time += 9
else:
    extra_time += 0
        
if program == "j":
    total_washing_time = total_washing_time + 40 
elif program == "u":
    total_washing_time = total_washing_time + 70
elif program == "s":
    total_washing_time = total_washing_time + 20
    # If the user has chosen to add an extra rinse, add 15 minutes to the total washing
    # time.
Result = total_washing_time + extra_time
print(f"total washing time is {Result}")