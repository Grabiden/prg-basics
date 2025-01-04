def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array                
print(bubblesort([4, 36, 12, 28, 9, 44, 5]))                