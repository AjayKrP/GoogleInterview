def reorder_array_by_index(arr, indexes):
    for i in range(len(arr)):
        tmp = arr[i]
        arr[i] = arr[indexes[i]]
        arr[indexes[i]] = tmp

    print(arr)

reorder_array_by_index([24, 56, 74, -23, 87, 91], [1, 2, 3, 0, 4, 5])
