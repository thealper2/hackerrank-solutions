if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = [_ for _ in arr]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]



    print(list(set(arr))[-2])