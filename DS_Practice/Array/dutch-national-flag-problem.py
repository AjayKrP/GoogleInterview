arr = [0, 0, 1, 1, 0, 0, 1, 0, 1]


def sort_2_color():
    li = 0
    hi = len(arr) - 1
    while li <= hi:
        if arr[li] == 0:
            li += 1
        else:
            arr[li], arr[hi] = arr[hi], arr[li]
            hi -= 1
    return arr


print(sort_2_color())

arr = [1, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1]


def sort_3_color():
    li = 0
    mi = 0
    hi = len(arr) - 1

    while mi <= hi:
        if arr[mi] == 0:
            arr[mi], arr[li] = arr[li], arr[mi]
            mi += 1
            li += 1
        elif arr[mi] == 1:
            mi += 1
        elif arr[mi] == 2:
            arr[mi], arr[hi] = arr[hi], arr[mi]
            hi -= 1
    return arr


print(sort_3_color())


"""
[0, 0, 0, 0, 0, 1, 1, 1, 1]
[0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
"""