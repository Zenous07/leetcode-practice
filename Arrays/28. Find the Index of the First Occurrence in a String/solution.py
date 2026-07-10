def firstIndex(haystack,needle):
    matched=False
    if len(needle)>len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i]==needle[0]:
            temp=i
            for j in range(len(needle)):
                if temp<len(haystack) and haystack[temp] == needle[j]:
                    temp+=1
                    if j==len(needle)-1:
                        matched=True
                else:
                    break
            if matched :
                return i
    return -1

print(firstIndex("leetcode","leeto"))