x = int(input("distance"))
y = int(input("hours"))
z = int(input("minutes"))
def avg_speed(distance,hours,minutes):
    minutes_total = hours * 60 + minutes
    result = (distance / minutes_total) * 60
    return result
print(avg_speed(x,y,z))