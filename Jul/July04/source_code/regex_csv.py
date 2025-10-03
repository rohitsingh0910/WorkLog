import re

lines = [
    "rohit,25,rohit@example.com",
    "john,abc,john@example",
    "amy,30,amy@site.org"
]

pat = re.compile(r'^[A-Za-z]+,\d{1,3},[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
print([bool(pat.match(l)) for l in lines])
