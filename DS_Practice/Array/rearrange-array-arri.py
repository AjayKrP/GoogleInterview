def rearrange_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] == i:
                arr[i], arr[j] = arr[j], arr[i]
    for i in range(len(arr)):
        if arr[i] != i:
            arr[i] = -1
    return arr


print(rearrange_array([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]))
