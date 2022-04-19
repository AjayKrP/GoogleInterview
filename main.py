class Professor:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name


class Subject:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name


class ProfessorSubjectAllocation:
    def __init__(self, professor_id, subject_id):
        self.__professor_id = professor_id
        self.__subject_id = subject_id


def helper(nums, idx, total, x):
    n = len(nums)
    if x < 0 or idx >= n:
        return 0

    if total == 0:
        return 0
    if total < 0:
        return -1

    val1 = helper(nums, idx + 1, total - nums[idx], x)
    val2 = helper(nums, idx, total - nums[x], x - 1)
    if val1 == -1 and val2 == -1:
        return -1
    return min(val1, val2) + 1


arr = [1, 1, 4, 2, 3]
print(helper(arr, 0, 5, len(arr) - 1))

arr = [5, 6, 7, 8, 9]
print(helper(arr, 0, 4, len(arr) - 1))


def convert_string_to_int(val):
    res = 0
    for c in val:
        res = res * 10 + (ord(c) - ord('0'))

    return res

def test_atoi():
    assert convert_string_to_int('123333333') == 123333333
print(convert_string_to_int('123333333'))
