#The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h.
# Write a program that prints a message when the specified car speed, read from the keyboard, has been exceeded.
# Sample result:
#Enter car speed: 38
#Warning: invalid car speed!!
car_speed = int(input("wprowadź prędkość "))
speed_limit_min = 40
speed_limit_max = 140
if car_speed < speed_limit_min:
    print("Warning: invalid car speed!!")
elif car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
