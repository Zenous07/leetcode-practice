def reverseVowels(s):
    vowels={'a','A','e','E','i','I','o','O','u','U'}
    l=0
    r=len(s)-1
    s=list(s)
    while l<=r:
        if s[l] not in vowels:
            l+=1
        elif s[r] not in vowels:
            r-=1
        else:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
    return ('').join(s)

print(reverseVowels("IceCreAm"))