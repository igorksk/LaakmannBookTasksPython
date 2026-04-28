"""Chapter 1 - String Rotation Check

Problem: Determine if one string is a rotation of another using a single
substring check (i.e., check if s2 is a substring of s1+s1).
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    # Two empty strings are rotations of each other
    if s1 == "" and s2 == "":
        return True
    return s2 in (s1 + s1)


if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print("Is '{}' a rotation of '{}'? {}".format(s2, s1, is_rotation(s1, s2)))