def remover(lista, val):
   return [value for value in lista if value != val]

def unique(arr):
    
    value = 0
    for item in arr:
        value = item
        if arr.count(value) > 1:
            remover(arr, value)

    return arr
print(unique([1,2,3,3,5,6,1]))       
