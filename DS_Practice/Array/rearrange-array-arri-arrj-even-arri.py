def rearrange_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i % 2 == 0:
                if arr[i] >= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[i] <= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr


print(rearrange_array([1, 2, 3, 4, 5, 6, 7]))
