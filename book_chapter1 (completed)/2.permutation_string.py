"""Chapter 1 - Check Permutation

Problem: Check whether one string is a permutation of another.

This module implements ``check_if_permutations`` that compares character
counts to determine if two strings are permutations of each other.
"""


def check_if_permutations(s1, s2):
    if len(s1) != len(s2):
        return False

    letters = {}
    for c in s1:
        letters[c] = letters.get(c, 0) + 1

    for c in s2:
        letters[c] = letters.get(c, 0) - 1
        if letters[c] < 0:
            return False

    return True


if __name__ == "__main__":
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")

    if check_if_permutations(s1, s2):
        print("Strings are permutations")
    else:
        print("Strings are not permutations")