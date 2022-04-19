class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        nums.append(0)
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        return 0


import functools


def helper(func):
    def wrapper(*args, **kwargs):
        res = func().split(' ')
        print(f'method name {func.__name__}, args: {args}, kwargs: {kwargs}')
        return res

    return wrapper


@helper
def myFunc(*args, **kwargs):
    return 'hello world!'


print(myFunc(["hello, world"], foo=2, bar=5))


def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p + q


x = fib(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
