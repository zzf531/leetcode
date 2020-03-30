def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    difference = len(str1) - len(str2)
    if difference == 0:
        return str1
    elif difference > 0:
        str1 = str1[len(str2):len(str1)]
    else:
        str2 = str2[len(str1):len(str2)]
    return gcdOfStrings(str1, str2)


print(gcdOfStrings('ABABAB', 'ABAB'))
