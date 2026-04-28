def maxNumberOfBalloons(text):
    balloon='balloon'
    s={}
    status=True

    for i in text:
        if i in balloon and i in s:
            s[i]+=1
        else:
            if i in balloon:
                s[i]=1
    for i in balloon:
        if i not in s:
            status=False
            break
    if not status:return 0

    if s['l']:
        s['l']=s['l']//2
    if s['o']:
        s['o']=s['o']//2

    return min(s.values())
        

print(maxNumberOfBalloons('nlaebolko'))