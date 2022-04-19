def rotate_arr(arr, k):
    for _ in range(k):
        for i in range(len(arr) - 1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


print(rotate_arr([1, 2, 3, 4, 5, 6, 7], 2))
