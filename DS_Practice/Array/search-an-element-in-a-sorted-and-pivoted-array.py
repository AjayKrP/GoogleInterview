# approach
"""
1. write a binary search method
2. Find the pivot => if left if greater and right is higher or vice versa
3. Check if element is greater than the pivot and smaller than the rightmost element or greater than the greater than
 the pivot and higher than leftmost element.

"""


def binary_search(arr, key) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
    return -1


def search(arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if arr[l] <= key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)

    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if arr[mid] <= key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)

arr = [3, 4, 5, 6, 7, 1, 2]
print(search(arr, 0, len(arr)-1, 1))
