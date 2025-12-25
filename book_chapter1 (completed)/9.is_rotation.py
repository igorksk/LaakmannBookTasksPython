def is_rotation(s1, s2):
    """
    Check if s2 is a rotation of s1 using only one call to is_substring.
    """
    if len(s1) != len(s2) or not s1:
        return False
    return s2 in (s1 + s1)

str1 = "waterbottle";
str2 = "erbottlewat";

print("Is '{}' a rotation of '{}'? {}".format(str2, str1, is_rotation(str1, str2)))