def cyclic_rotate_arr(arr, k):
    for _ in range(k):
        tmp = arr[len(arr) - 1]
        for i in range(len(arr) - 1 - _, 0, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        arr[0] = tmp
    return arr


print(cyclic_rotate_arr([1, 2, 3, 4, 5, 6, 7], 2))