import re
import sys

n = int(input())
for line in sys.stdin:
    line = re.sub(r"(?<= )(&&)(?= )", "and", line)
    line = re.sub(r"(?<= )(\|\|)(?= )", "or", line)
    print(line, end="")