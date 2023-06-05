# def filter_wordlist(wordlist, min_length):
#     filtered_wordlist = []
#     for word in wordlist:
#         if len(word) >= min_length:
#             filtered_wordlist.append(word)
#     return filtered_wordlist

# # Read wordlist from file
# input_file_path = 'x.txt'  # Replace with the actual input file path

# with open(input_file_path, 'r') as input_file:
#     wordlist = input_file.read().splitlines()

# # Get user input for the minimum length
# min_length = int(input("Enter the minimum length for words: "))

# # Filter wordlist based on minimum length
# filtered_wordlist = filter_wordlist(wordlist, min_length)

# # Save the filtered wordlist back to the file
# with open(input_file_path, 'w') as output_file:
#     output_file.write('\n'.join(filtered_wordlist))

# Read wordlist from file
input_file_path = 'aiden.txt'  # Replace with the actual input file path

with open(input_file_path, 'r') as input_file:
    wordlist = input_file.read().splitlines()

# Filter wordlist based on the "+" symbol
filtered_wordlist = [line for line in wordlist if '+' in line]

# Save the filtered wordlist back to the file
with open(input_file_path, 'w') as output_file:
    output_file.write('\n'.join(filtered_wordlist))
