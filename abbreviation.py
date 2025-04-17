# https://www.youtube.com/watch?v=ViILdd8495M
def abbreviation(a, b):
    """Determine if string `a` can be converted to string `b` by deleting lowercase letters and capitalizing some letters. 
    Uses a 2D DP table of size (n+1) x (m+1) to track valid transformations."""
    n = len(a)
    m = len(b)

    # Create dp table of size (n+1) x (m+1) filled with False
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True  # Empty 'a' can be transformed to empty 'b'

    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                # Option 1: Delete lowercase character
                if a[i].islower():
                    dp[i + 1][j] = True
                    print(f"Deleting '{a[i]}' at a[{i}], dp[{i+1}][{j}] = True")
                # Option 2: Match if capitalized character matches b[j]
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                    print(f"Matching '{a[i]}' to '{b[j]}' at a[{i}], b[{j}], dp[{i+1}][{j+1}] = True")

    # Print the dp table
    print("\nFinal DP Table:")
    for row in dp:
        print(row)

    return "YES" if dp[n][m] else "NO"

a = "daBcd"
b = "ABC"
print("Result:", abbreviation(a, b))