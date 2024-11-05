#Write a program that allows you to convert time in 24-hour format to 12-hour format.
#The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

T = input("wpisz godzine (XX:YY) ")
H, M = map(int, T.split(":"))

if H >= 12:
    period = "pm"
else:
    period = "am"

if H == 0:
   H_12 = 12
elif H > 12:
    H_12 = H - 12
else:
    H_12 = H

print(f"{H_12}:{M}{period}")    
