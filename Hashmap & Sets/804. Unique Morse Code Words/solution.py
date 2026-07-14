def uniqueMorseCodes(words):
    d={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
    s=set()
    for word in words:
        temp=""
        for i in word:
            temp+=("").join(d[i])
        s.add(temp)
    return len(s)

print(uniqueMorseCodes(["gin","zen","gig","msg"]))