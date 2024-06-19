import textwrap

def wrap(string, max_width):
    a = len(string) % max_width
    res = []
    for i in range(0, len(string)-max_width, max_width):
        res.append(string[i:i+max_width])

    if a != 0:
        res.append(string[-a:])
    return '\n'.join(res)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)