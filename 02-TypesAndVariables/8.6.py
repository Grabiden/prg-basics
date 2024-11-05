# Function to convert decimal to binary and hexadecimal

    # Read an integer from the user
decimal_number = int(input("Enter an integer number: "))
    
    # Convert to binary using bin() and remove the '0b' prefix
binary_number = bin(decimal_number)[2:]
    
    # Convert to hexadecimal using hex() and remove the '0x' prefix
hexadecimal_number = hex(decimal_number)[2:].upper()  # Convert to uppercase for better readability
    
    # Print the results
print(f"Decimal: {decimal_number}")
print(f"Binary: {binary_number}")
print(f"Hexadecimal: {hexadecimal_number}")

