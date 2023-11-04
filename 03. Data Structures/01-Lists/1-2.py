def is_unique(string):
    # Create an empty set to store seen characters
    seen = set()

    for char in string:
        if char in seen:
            return False
        seen.add(char)

    return True

def is_unique(string):
    length = len(string)

    for i in range(length):
        for j in range(i + 1, length):
            if string[i] == string[j]:
                return False

    return True
