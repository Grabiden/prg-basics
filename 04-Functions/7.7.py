def binary_number(a):
    p = set(a)
    s = {"1", "0"}
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")

result = binary_number("101201")
print(result)        