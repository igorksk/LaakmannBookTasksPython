"""Chapter 1 - Replace Spaces (URLify)

Problem: Replace spaces in a character array with '%20' up to the true
length of the string. This simulates the URLify operation in-place.
"""

def replace_spaces(char_array, true_length):
    # Count spaces in the first trueLength characters
    space_count = 0
    for i in range(true_length):
        if char_array[i] == ' ':
            space_count += 1

    # Calculate the new index after replacements
    new_index = true_length + space_count * 2

    # If the array is longer, put a null character at the end
    if new_index < len(char_array):
        char_array[new_index] = '\0'

    # Fill the array backwards
    i = true_length - 1
    while i >= 0:
        if char_array[i] == ' ':
            char_array[new_index - 1] = '0'
            char_array[new_index - 2] = '2'
            char_array[new_index - 3] = '%'
            new_index -= 3
        else:
            char_array[new_index - 1] = char_array[i]
            new_index -= 1
        i -= 1

# Prepare input array with extra space
input_chars = [
    'M', 'r', ' ', 'J', 'o', 'h', 'n', ' ',
    'S', 'm', 'i', 't', 'h',
    '\0', '\0', '\0', '\0'
]
true_length = 13

replace_spaces(input_chars, true_length)

# Convert back to string
output_string = ''.join(input_chars).rstrip('\0')
print(output_string)