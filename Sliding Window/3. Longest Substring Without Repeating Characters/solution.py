def longestWithoutRepeating(s):
    seen=set()
    l=0
    result=0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[l])
            l+=1
        seen.add(s[i])
        result=max(result,i-l+1)
    return result

print(longestWithoutRepeating("ababcbb"))