n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        print(int(int(a) / int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)