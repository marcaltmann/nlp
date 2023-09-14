import re

r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])(morn[gin']{0,3}|"
r += r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
re_greeting = re.compile(r, flags=re.IGNORECASE)

while True:
    user_input = input('Input: ')
    match = re_greeting.match(user_input)
    print(match)
