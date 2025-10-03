import re
from collections import Counter

log = """
127.0.0.1 - - [24/Jul/2025:10:10:10] "GET /index HTTP/1.1" 200 2326
10.0.0.2 - - [24/Jul/2025:10:10:11] "POST /login HTTP/1.1" 401 512
127.0.0.1 - - [24/Jul/2025:10:10:12] "GET /home HTTP/1.1" 200 1200
"""

ips = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', log)
codes = re.findall(r'"\s*(\d{3})\s', log)
print(Counter(ips))
print(Counter(codes))
