str1 = input("Enter string 1: ")

str2 = input("Enter string 2: ")

def check_if_permutations(str1, str2):

    if len(str1) != len(str2):
        return False;

    letters = {}

    for c in str1:
        letters[c] = letters.get(c, 0) + 1

    for c in str2:
        letters[c] = letters.get(c, 0) - 1
        if letters[c] < 0:
            return False

    return True;

if check_if_permutations(str1, str2):
    print("Strings are permutations")
else:
    print("Strings are not permutations")