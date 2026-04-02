def hvlcs(s1:str, s2:str, values:dict[str, int]):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = values[s1[i - 1]] + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    max_val = dp[n][m]

    chars = []
    while n > 0 and m > 0:
        if s1[n - 1] == s2[m - 1] and dp[n][m] == dp[n - 1][m - 1] + values[s1[n - 1]]:
            chars.append(s1[n - 1])
            n -= 1
            m -= 1
        elif dp[n - 1][m] >= dp[n][m - 1]:
            n -= 1
        else:
            m -= 1
    chars.reverse()

    return max_val, "".join(chars)