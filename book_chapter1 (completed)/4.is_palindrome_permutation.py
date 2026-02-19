"""Chapter 1 - Palindrome Permutation

Problem: Given a string, check if any permutation of the string is a
palindrome (ignoring spaces and case).
"""

str = "Tact Coa"

def is_palindrome_permutation(str):

    from collections import defaultdict

    counts = defaultdict(int)

    for symbol in str:
        if symbol == ' ':
            continue  # Ignore spaces

        lower_symbol = symbol.lower()

        counts[lower_symbol] += 1

    odd_count = 0

    for count in counts.values():
        if count % 2 == 1:
            odd_count += 1

    # Can be only 0 or 1 odd chars count
    return odd_count < 2

print(is_palindrome_permutation(str))