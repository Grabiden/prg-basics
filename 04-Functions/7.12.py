#Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

#f(4) returns "*/*/*/*"
#f(1) returns "*"
def f(n):
    result = "*/"*(n-1) + "*"
    return result
fiut = f(4)
print(fiut) # Output: */*/*/*/
