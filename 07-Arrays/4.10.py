ar1 = [4,36,12,28,9,44,5]
ar2 = [5,1,36]
k = 0
n = len(ar2) 
while k < n:
    y = ar2[k]
    if y in ar1:
        ar1.remove(y)
    k += 1    
    
print(ar1)    