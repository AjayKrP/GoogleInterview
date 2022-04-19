from collections import Counter


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result


def sliding_window(s, t):
    needs = Counter(t)
    minLen = float('inf')
    left = right = start = 0
    s = list(s)
    window = {}
    for char in t:
        window[char] = 0

    match = 0
    while right < len(s):
        c1 = s[right]
        if c1 in needs:
            window[c1] += 1
            if window[c1] == needs[c1]:
                match += 1
        right += 1
        while match == len(needs):
            if right - left < minLen:
                start = left
                minLen = right - left
            c2 = s[left]
            if c2 in needs:
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            left += 1
        return "" if minLen == float('inf') else ''.join(s[start: minLen])


class Solution1:
    def maxSlidingWindow(self, nums, k: int):
        lastMax = max(nums[:k])
        for i in range(k, len(nums)):
            lastMax = max(lastMax, nums[i])
        return lastMax


from collections import deque

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        for i in range(k):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        ans = [nums[dq[0]]]
        for i in range(k, len(nums)):
            if i - dq[0] == k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans


def base62(num):
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num:
        num, carry = divmod(num, 62)
        result += BASE62[carry]
    return result


print(base62(11187))


def distinct_string(string, k):
    window = {}
    left = 0
    res = float('-inf')
    for i in range(len(string)):
        if string[i] not in window:
            window[string[i]] = 1
        else:
            window[string[i]] += 1
        while len(window) > k:
            window[string[left]] -= 1
            if window[string[left]] == 0:
                window.pop(string[left], None)
            left += 1
        res = max(res, i - left + 1)

    return res


print(distinct_string('araaci', 1))
print(distinct_string('araaci', 2))
print(distinct_string('cbbebi', 3))
