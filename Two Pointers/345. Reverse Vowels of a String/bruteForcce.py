def reverseVowels(s):
    vowels={'a','A','e','E','i','I','o','O','u','U'}
    pos=[]
    s=list(s)
    for i in s:
        if i in vowels:
            pos.append(i)
    for i in range(len(s)):
        if s[i] in vowels:
            s[i]=pos.pop()
    return ('').join(s)

print(reverseVowels("IceCreAm"))