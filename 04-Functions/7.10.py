#Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:

#f(-7,8) returns 3
#f(-1,11) returns 0
def f(x, y):
    count = 0

    for nuber in range(x +1, y):
        if nuber % 2 == 0 and nuber < 0:
            count += 1
    return count