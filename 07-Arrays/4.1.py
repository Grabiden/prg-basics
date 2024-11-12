#An array contains integer numbers: 34,7,19,4,21,8.
# Create a program that calculates and prints the number of even values in the array. Use the ‘while’ loop statement.
arr = [34,7,19,4,21,8]
n = 0
arr_even = []
while n < len(arr):
    if arr[n] % 2 == 0:
        arr_even.append(arr[n])
    n +=1    
print(sum(arr_even))    
