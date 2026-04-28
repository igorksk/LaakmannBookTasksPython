"""Chapter 1 - Unique Characters

Problem: Determine if a string has all unique characters.

This module provides two approaches:
- ``unique_without_data_structures``: O(n^2) pairwise comparison
- ``unique_using_dictionary``: uses a dictionary to detect duplicates
"""

def unique_without_data_structures(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def unique_using_dictionary(s):
    seen = {}
    for ch in s:
        if ch in seen:
            return False
        seen[ch] = True
    return True


if __name__ == "__main__":
    s = input("Enter string: ")

    if unique_without_data_structures(s):
        print("Symbols unique by first check")
    else:
        print("Symbols not unique by first check")

    if unique_using_dictionary(s):
        print("Symbols unique by second check")
    else:
        print("Symbols not unique by second check")
