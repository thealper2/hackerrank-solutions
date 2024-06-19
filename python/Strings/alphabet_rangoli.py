def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    lines = []
    
    for i in range(n):
        s = "-".join(alpha[i:n])
        lines.append((s[::-1] + s[1:]).center(4*n-3, "-"))
    
    print("\n".join(lines[::-1] + lines[1:]))   
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)