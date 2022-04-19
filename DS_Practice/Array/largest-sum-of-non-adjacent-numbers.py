def largest_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = max(arr[1], arr[0])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
    print(dp)
    return dp[-1]


print(largest_sum([4, 2, 3, 5, 1, 6, 7]))
print(largest_sum([5, 20, 15, -2, 18]))
print(largest_sum([4, 1, 6, 3, 2]))
