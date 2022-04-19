def rearrange_array_order_smallest_largest(arr):
    arr.sort()
    n = len(arr)
    i = 1
    j = n - 1
    while i <= n // 2 < j:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1
    return arr


print(rearrange_array_order_smallest_largest([5, 8, 1, 4, 2, 9, 3, 7, 6]))
