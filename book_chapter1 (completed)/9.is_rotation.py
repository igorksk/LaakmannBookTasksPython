"""Chapter 1 - String Rotation Check

Problem: Determine if one string is a rotation of another using a single
substring check (i.e., check if s2 is a substring of s1+s1).
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2) or not s1:
        return False
    return s2 in (s1 + s1)

str1 = "waterbottle";
str2 = "erbottlewat";

print("Is '{}' a rotation of '{}'? {}".format(str2, str1, is_rotation(str1, str2)))