def isAnagram(s,t):
    if len(s) != len(t):return False
    count={}

    for c in s:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
    
    for c in t:
        if c not in count:
            return False
        if count[c] <=0:
            return False
        else:
            count[c]-=1
    return True

print(isAnagram("anagram","nagaram"))