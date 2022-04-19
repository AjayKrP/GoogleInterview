arr = [0, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6]


def binary_search(target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    return -1


def binary_search_left_boundary(target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    if l >= len(arr) or arr[l] != target:
        return -1
    return l


def binary_search_right_boundary(target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
    if r < 0 or arr[r] != target:
        return -1
    return r


print(binary_search(2))
print(binary_search_left_boundary(-1))
res = binary_search_right_boundary(3)
assert arr[res] == 3
print(arr[res])
