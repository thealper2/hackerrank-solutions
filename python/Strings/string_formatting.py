def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        binary = bin(i)[2:]
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        print(f'{str(i):>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}')
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)