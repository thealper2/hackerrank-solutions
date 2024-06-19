width = int(input())
char = 'H'

for i in range(width):
    print(f'{char * i}'.rjust(width - 1) + char + f'{char * i}'.ljust(width - 1))

for i in range(width + 1):
    print(f'{char * width}'.center(width * 2) + f'{char * width}'.center(width * 6))

for i in range((width + 1) // 2):
    print(f'{char * width * 5}'.center(width * 6))

for i in range(width + 1):
    print(f'{char * width}'.center(width * 2) + f'{char * width}'.center(width * 6))

for i in range(width):
    w = width - i - 1
    s = f'{char * w}'.rjust(width) + char + f'{char * w}'.ljust(width)
    print(s.rjust(width * 6))