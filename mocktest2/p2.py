def f(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for j in dict:
        if dict[j] == 1:
            return j  
print(f([7,7,7,7,7,5,7,7]))     
