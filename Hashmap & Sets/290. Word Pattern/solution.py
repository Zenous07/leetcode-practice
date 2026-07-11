def wordPattern(pattern,s):
    s=s.split()
    if len(s) != len(pattern):
        return False
    p=dict()
    sd=dict()
    for i in range(len(pattern)):
        if pattern[i] not in p:
            if s[i] not in sd:
                p[pattern[i]]=s[i]
                sd[s[i]]=pattern[i]
            else:
                return False
        else:
            if p[pattern[i]]!=s[i]:
                return False
    return True

print(wordPattern("abba","dog cat cat dog"))