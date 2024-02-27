import string


def isPalindrome(s: str) -> bool:
    digits = list(map(lambda n: str(n), range(10)))
    t = ""
    for ch in s:
        if ch in string.ascii_lowercase:
            t += ch
        elif ch in string.ascii_uppercase:
            t += ch.lower()
        elif ch in digits:
            t += ch
    return t == t[::-1]
