def find_max_non_adjacent_element_sum(arr):
    n = len(arr)
    dp = [0 for _ in range(n + 1)]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
    return dp[-2]


def test_max_sum():
    assert find_max_non_adjacent_element_sum([5, 20, 15, -2, 18]) == 38
    assert find_max_non_adjacent_element_sum([4, 1, 6, 3, 2]) == 12
