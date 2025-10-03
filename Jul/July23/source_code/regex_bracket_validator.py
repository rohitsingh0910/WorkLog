import re

def valid(s):
    s = re.sub(r'[^()\[\]{}]', '', s)
    stack = []
    m = {')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != m[ch]:
                return False
            stack.pop()
    return not stack

print(valid("{a(b[c]d)e}"))
print(valid("{a(b[c}d)e}"))
