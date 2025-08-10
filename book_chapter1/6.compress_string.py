input_str = input("Enter string: ")

def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            count = 1

    # Add the last character and its count
    compressed.append(s[-1])
    compressed.append(str(count))

    compressed_string = ''.join(compressed)
    
    return compressed_string if len(compressed_string) < len(s) else s

print("Compressed string:", compress_string(input_str))