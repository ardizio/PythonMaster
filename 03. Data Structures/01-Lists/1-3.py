def is_permutation(str1, str2):
    # Check if the lengths of the strings are different; if they are, they can't be permutations.
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character counts for both strings.
    char_count1 = {}
    char_count2 = {}

    # Count characters in the first string.
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    # Count characters in the second string.
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare the character counts of both strings.
    return char_count1 == char_count2

# Example usage:
str1 = "abc"
str2 = "bca"
print(is_permutation(str1, str2))  # True

str1 = "abc"
str2 = "def"
print(is_permutation(str1, str2))  # False
