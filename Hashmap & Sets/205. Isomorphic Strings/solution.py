def isomorphicStrings(s,t):
    if len(s) != len(t):
        return False
    ds=dict()
    st=dict()
    for i in range(len(s)):
        if s[i] not in ds:
            if t[i] not in st:
                ds[s[i]]=t[i]
                st[t[i]]=s[i]
            else:
                return False
        else:
            if ds[s[i]]!=t[i]:
                return False
    return True

print(isomorphicStrings("egg","add"))