"""
If array is not sorted then we can use hashtable method
"""
def two_sum(arr, target):
    visited = set()
    for i in range(len(arr)):
        diff = target - arr[i]
        if arr[i] not in visited:
            visited.add(diff)
        else:
            return [diff, arr[i]]
    return [-1, -1]


def two_sum_without_hashtable(arr, target):
    i = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            break
    n = len(arr)
    # r is now index of highest element
    r = i
    # l is now index of smallest element
    l = (i + 1) % n
    while l != r:
        if arr[l] + arr[r] == target:
            return True
        # If current pair sum is less, move to the higher sum
        if arr[l] + arr[r] < target:
            l = (l + 1) % n
        else:
            # Move to the lower sum side
            r = (r + n - 1) % n
    return False


print(two_sum_without_hashtable([11, 9, 15, 6, 8, 9, 10], 24))
