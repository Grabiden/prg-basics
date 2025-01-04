def remover(lista, val):
   return [value for value in lista if value != val]
array = [1,2,30,50,70]

array.sort()
array.reverse()
def I(array):
   druga_najwieksza = 0

   if len(array) < 2:
      druga_najwieksza = array[0]
   else:
      druga_najwieksza = array[1]

   return print(f"druga największa to {druga_najwieksza}")
def II(array):
   max_value = max(array)
   min_value = min(array)
   różnica = max_value - min_value
   return różnica
def III(array):
    mediana = 0
    if len(array)%2 == 0:
       mediana = (array[len(array)//2 - 1] + array[len(array)//2])
    else:
       mediana = array[len(array)//2]
    return mediana

print(I(array))
print(II(array))
print(III(array))


