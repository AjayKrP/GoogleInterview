def merge_arrays(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)

    i = j = 0

    arr3 = []
    while i < l1 and j < l2:
        if arr1[i] > arr2[j]:
            arr3.append(arr2[j])
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1
    while i < l1:
        arr3.append(arr1[i])
        i += 1
    while j < l2:
        arr3.append(arr2[j])
        j += 1

    return arr3


print(merge_arrays([1, 3, 4, 5], [2, 4, 6, 8]))
