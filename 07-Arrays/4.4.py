# Given array
numbers = [-15, 8, -31, 47, -2, 19]

# Initialize max and min with the first element of the array
max_number = numbers[0]
min_number = numbers[0]

# Iterate through the array to find max and min
for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

# Print the results
print("Maximum number:", max_number)
print("Minimum number:", min_number)