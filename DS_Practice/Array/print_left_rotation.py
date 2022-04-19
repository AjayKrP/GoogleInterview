def print_left_rotation(arr, k):
    mod = k % len(arr)

    for i in range(len(arr)):
        print(arr[(i + mod) % len(arr)], end=' ')


print_left_rotation([1, 3, 5, 7, 9], 2)
