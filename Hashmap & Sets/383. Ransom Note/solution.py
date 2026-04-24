def ransomNote(ransomNote,magazine):
    count={}
    
    for c in magazine:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
    
    for c in ransomNote:
        if c in count and count[c]>0:
            count[c]-=1
        else:
            return False
    return True



print(ransomNote('aa','ab'))