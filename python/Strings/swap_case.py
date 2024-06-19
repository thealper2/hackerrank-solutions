def swap_case(s):
    new = ''
    for char in s:
        if char.isupper():
            new += char.lower()
        elif char.islower():
            new += char.upper()
        else:
            new += char
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)