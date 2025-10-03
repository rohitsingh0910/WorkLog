import re

def normalize(s):
    def repl(m):
        d, mth, y = m.group(1), m.group(2), m.group(3)
        if len(y) == 2:
            y = "20" + y
        return f"{y}-{int(mth):02d}-{int(d):02d}"
    return re.sub(r'\b(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})\b', repl, s)

print(normalize("Today is 1/7/25, yesterday was 30-06-2025"))
