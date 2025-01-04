x = list(input("binary"))
y = []
for i in x:
    if i == "0":
        y.append(1)
    else:
        y.append(0)
print(y)        