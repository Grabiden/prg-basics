#Define the function f(n), which returns numbers from 1 to n as a string. Sample result:

#f(11) returns "1234567891011"
#f(4) returns "1234"
def f(n):
    return "".join(str(i) for i in range(1, n+1))
#Test the function with n = 11 and n = 4
print(f(11)) # Output: "1234567891011"