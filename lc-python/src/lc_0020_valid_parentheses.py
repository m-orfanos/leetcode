def isValid(s: str) -> bool:
    """
    Keep track of the opening braces in a list/stack. When a closing brace is
    found, check against the most recent opening brace.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if len(s) % 2 == 1:
        return False
    tokens = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if len(stack) == 0 or tokens[stack.pop()] != ch:
                return False
    return len(stack) == 0
