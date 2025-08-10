

def are_one_edit_apart(s1, s2):
    if len(s1) == len(s2):
        return one_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_insert(s1, s2)
    elif len(s1) == len(s2) + 1:
        return one_insert(s2, s1)
    return False

def one_replace(s1, s2):
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_insert(s1, s2):
    index1 = 0
    index2 = 0
    found_difference = False
    
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True
            index2 += 1  # Move pointer in the longer string
        else:
            index1 += 1
            index2 += 1
            
    return True

str1 = input("Enter string 1: ")

str2 = input("Enter string 2: ")

print("Are the two strings one edit apart?", are_one_edit_apart(str1, str2))