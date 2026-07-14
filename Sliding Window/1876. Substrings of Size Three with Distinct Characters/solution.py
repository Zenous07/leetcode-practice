def distinct3substring(s):
    if len(s)<3:
        return 0
    seen=set()
    count=0
    l=0
    for r in range(len(s)):
        if s[r] not in seen:
            if len(seen)==3:
                seen.remove(s[l])
                l+=1
                seen.add(s[r])
                if len(seen)==3:
                    count+=1
            else:
                seen.add(s[r])
                if len(seen)==3:
                    count+=1
                
        else:
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            if len(seen)==3:
                count+=1
    return count

print(distinct3substring("aababcabc"))