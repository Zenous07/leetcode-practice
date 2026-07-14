def distinct3substring(s):
    if len(s)<3:
        return 0
    seen=set()
    count=0
    l=0
    for r in range(len(s)):
        