def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage

fiut = [1, 4, 7, 4, 5, 8, 9]
result = bubble_sort(fiut)
print(result)