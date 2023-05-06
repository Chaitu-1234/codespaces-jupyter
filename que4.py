def first_non_repeated_char(s):
    char_counts = {}
    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    for c in s:
        if char_counts[c] == 1:
            return c
    return None

s = input('Enter Characters')
result = first_non_repeated_char(s)
if result is not None:
    print("The first non-repeated character in the string is:", result)
else:
    print("There are no non-repeated characters in the string.")
