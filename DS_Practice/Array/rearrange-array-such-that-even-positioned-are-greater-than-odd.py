def rearrange_array(arr):
    for i in range(1, len(arr)):
        if i % 2 == 0 and arr[i] >= arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        elif i % 2 != 0 and arr[i] <= arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    print(arr)


rearrange_array([1, 2, 2, 1])
rearrange_array([1,2,3])
