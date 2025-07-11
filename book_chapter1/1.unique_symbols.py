str = input("Enter string: ")

def unique_without_data_structures(str):

    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False

    return True;

def unique_using_dictionary(str):

    dict = {}

    for s in str:
        if s in dict:
            return False;

        dict[s] = s

    return True;

if unique_without_data_structures(str):
    print("Symbols unique by first check")
else:
    print("Symbols not unique by first check")

if unique_using_dictionary(str):
    print("Symbols unique by second check")
else:
    print("Symbols not unique by second check")
