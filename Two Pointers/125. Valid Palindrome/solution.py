def palindrome(s):
    s = s.lower()
    s = "".join(c for c in s if c.isalnum())
    if s==s[::-1]: return True
    return False


print(palindrome("A man, a plan, a canal: Panama"))