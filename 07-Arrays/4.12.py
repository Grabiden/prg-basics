def remove_non_unique_elements(arr):
    # Create a dictionary to count occurrences of each element
    count = {}
    
    # Count each element in the array
    for element in arr:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
            
    # Create a new list for unique elements
    unique_elements = [element for element in arr if count[element] == 1]
    
    return unique_elements

# Example usage
if __name__ == "__main__":
    # Input array
    array = [1, 2, 3, 2, 4, 3, 5, 1, 6]
    
    unique_elements = remove_non_unique_elements(array)
    print("Unique elements in the array (only those that appear exactly once):")
    print(unique_elements)


        