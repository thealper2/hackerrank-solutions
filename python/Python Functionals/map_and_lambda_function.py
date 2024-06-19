cube = lambda x: x * x * x

def fibonacci(n):
    arr = [0, 1]
    if n < 2:
        return arr[:n]
    
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))