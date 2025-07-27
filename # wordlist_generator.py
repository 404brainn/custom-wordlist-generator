# wordlist_generator.py

import itertools

# Get user input
first_name = input("Enter first name: ")
nickname = input("Enter nickname: ")
birth_year = input("Enter birth year (e.g. 2000): ")
special_chars = ['@', '!', '#', '$']

base_words = [first_name, nickname, birth_year]
combinations = []

# Basic combinations
for word in base_words:
    combinations.append(word)
    combinations.append(word.lower())
    combinations.append(word.upper())

# Combine words
for a, b in itertools.permutations(base_words, 2):
    combinations.append(a + b)
    combinations.append(b + a)

# Add special characters and numbers
final_list = []
for word in combinations:
    for char in special_chars:
        final_list.append(word + char)
        final_list.append(char + word)
        final_list.append(word + char + "123")

# Remove duplicates
final_list = list(set(final_list))

# Save to file
with open("custom_wordlist.txt", "w") as f:
    for word in final_list:
        f.write(word + "\n")

print(f"\n[+] Wordlist created: custom_wordlist.txt")
