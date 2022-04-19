def max_balanced_string(word):
    word = list(word)
    ans = 0
    left = 0
    right = 0
    for i in range(len(word)):
        if word[i] == 'L':
            left += 1
        if word[i] == 'R':
            right += 1
        if left == right:
            ans += 1
    return ans

