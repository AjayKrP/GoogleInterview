def fine_left_boundary(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            r = m - 1  # shrink right
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1

    if l >= len(arr) or arr[l] != target:
        return -1
    return l


def find_right_boundary(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            l = m + 1  # shrink left
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1

    if r < 0 or arr[r] != target:
        return -1
    return r


def find_occurrences(arr, target):
    right = find_right_boundary(arr, target)
    left = fine_left_boundary(arr, target)
    if left == -1 and right == -1:
        return 0
    return right - left + 1


def test_find_occurrences():
    assert find_occurrences([4, 4, 8, 8, 8, 15, 16, 23, 23, 42], 8) == 3
    assert find_occurrences([3, 5, 5, 5, 5, 7, 8, 8], 6) == 0
    assert find_occurrences([3, 5, 5, 5, 5, 7, 8, 8], 5) == 4


"""
def count(arr, target):
  n = len(arr)
  left = bisect_left(arr, target, 0, n)
  right = bisect_right(arr, target, left, n)  # use left as a lower bound
  return right - left

def bisect_left(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo

def bisect_right(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
"""
