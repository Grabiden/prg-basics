text = "This is a sample text."
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
i = 0 

# Count vowels in the text
while i < len(text):
    if text[i].lower() in vowels:  # Check for vowels in a case-insensitive manner
        vowel_count += 1  # Use += to increment the count
    i += 1  # Move to the next character

print(f"The number of vowels in the text is: {vowel_count}")