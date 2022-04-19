def find_duplicates(arr):
    N = len(arr)
    for i in range(N):
        x = arr[i] % N
        arr[x] += N

    for i in range(N):
        if arr[i] >= N * 2:
            print(i)


find_duplicates([0, 4, 3, 2, 7, 8, 2, 3, 1])
