def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False

str1 = input('enter first string')
str2 = input('enter second string')
if is_rotation(str1, str2):
    print("The strings are a rotation of each other.")
else:
    print("The strings are not a rotation of each other.")
