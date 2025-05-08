'''Write a program that prompts the user for a sentence and
displays the number of vowels in the sentence.'''

# Prompt the user for a sentence
sentence = input("Please enter a sentence: ")

# Initialize a counter for vowels
vowel_count = 0

# Define a set of vowels
vowels = set("aeiouAEIOU")

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is a vowel
    if char in vowels:
        # Increment the vowel counter
        vowel_count += 1