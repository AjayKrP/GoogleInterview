def find_minimum_maximum(arr):
    min_element = float('inf')
    max_element = float('-inf')

    for i in range(len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
        if arr[i] > max_element:
            max_element = arr[i]

    return min_element, max_element


def find_minimum_maximum_divide_conquer(arr, l, r):
    if l == r:
        return arr[l], arr[r]

    if l + 1 == r:
        if arr[l] > arr[r]:
            return arr[r], arr[l]
        else:
            return arr[l], arr[r]

    mid = (r + l) // 2
    li = find_minimum_maximum_divide_conquer(arr, 0, mid)
    ri = find_minimum_maximum_divide_conquer(arr, mid + 1, r)

    return min(li[0], ri[0]), max(li[1], ri[1])


def test_find_minimum_maximum():
    assert find_minimum_maximum([3, 5, 2, 56, 7, 3]) == (2, 56)
    arr1 = [3, 5, 2, 56, 7, 3]
    assert find_minimum_maximum_divide_conquer(arr1, 0, len(arr1) - 1) == (2, 56)
