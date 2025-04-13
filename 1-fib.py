# key take away here recursion + memorization
# since the num times the recursion will be called
# is n times (returned from the dict otherwise)
# time complexity is O(n)

memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result

print(fib(80))
print(len(memo))
print(memo)
