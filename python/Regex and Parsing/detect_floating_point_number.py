import re

pattern = re.compile("^[-+]?\d*\.\d+$")
for _ in range(int(input())):
    word = input()
    if pattern.match(word):
        print(True)
    else:
        print(False)