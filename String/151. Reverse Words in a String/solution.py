def reverseWordsInString(s):
    s=s.split()
    s=s[::-1]
    return '*'.join(s)

print(reverseWordsInString("  hello   world  "))