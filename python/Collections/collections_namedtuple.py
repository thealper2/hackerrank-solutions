from collections import namedtuple

n = int(input())
colnames = ' '.join(input().split())
Student = namedtuple('Student', colnames)

marks = 0
for _ in range(n):
    s = Student._make(input().split())
    marks += int(s.MARKS)

print(round(marks / n, 2))