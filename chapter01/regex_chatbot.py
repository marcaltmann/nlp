import re

r = '(hi|hello|hey)[ ,:.!]*([a-z]*)'
m = re.match(r, 'Hello Rosa', flags=re.IGNORECASE)
print(m)
m = re.match(r, "hi ho, hi ho, it's off to work...", flags=re.IGNORECASE)
print(m)
m = re.match(r, "hey, what's up", flags=re.IGNORECASE)
print(m)
