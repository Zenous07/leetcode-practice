def romanToInt(s):
    sum=0
    sym={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(0,len(s)):
        if i<len(s)-1 and sym.get(s[i+1])>sym.get(s[i]):
            sum-=sym.get(s[i])
        else:
            sum+=sym.get(s[i])
    return sum

print(romanToInt("MCMXCIV"))