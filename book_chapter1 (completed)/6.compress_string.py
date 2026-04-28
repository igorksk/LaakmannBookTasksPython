"""Chapter 1 - String Compression

Problem: Perform basic string compression using counts of repeated
characters (e.g., aabcccccaaa -> a2b1c5a3). Return original if compressed
string is not smaller.
"""

def compress_string(s):
    if not s:
        return s

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


if __name__ == "__main__":
    input_str = input("Enter string: ")
    print("Compressed string:", compress_string(input_str))