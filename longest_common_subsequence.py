def longestCommonSubsequence(s1, s2):
    
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1) + 1)]

    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) -1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i+1][j])

    return dp[0][0]

def longestCommonSubsequenceStrings(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    i, j = 0, 0
    result = []
    while i < n and j < m:
        if s1[i] == s2[j]:
            result.append(s1[i])
            i += 1
            j += 1
        elif dp[i+1][j] >= dp[i][j+1]:
            i += 1
        else:
            j += 1

    return ''.join(result)
    
print(longestCommonSubsequence("ace", "abcde"))

print(longestCommonSubsequenceStrings("ace", "abcde"))  # Output: "ace"
print(longestCommonSubsequenceStrings("AGGTAB", "GXTXAYB"))  # Output: "GTAB"

