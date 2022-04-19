"""
Move all zeros to the end of array by swapping
"""
def move_zeros_to_end(arr):
    right = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] == 0 and i is not right:
            for j in range(i, right):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            arr[right] = 0
            right -= 1
    return arr


def move_zeros_to_end_by_count_method(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

"""
Move zeros to end by single pass
"""
def move_zeros_by_single_pass(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr



print(move_zeros_by_single_pass([1, 2, 0, 4, 3, 0, 5, 0]))
