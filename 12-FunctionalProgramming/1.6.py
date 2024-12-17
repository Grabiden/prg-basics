x = int(input("distance"))
y = int(input("hours"))
z = int(input("minutes"))
avg_speed = lambda x,y,z: (x / (y*60+z)) * 60
print(avg_speed(x,y,z))