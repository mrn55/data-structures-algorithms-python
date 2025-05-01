def checkSubarraySum(self, nums, k):
    remainder = {0: -1}
    total = 0

    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder > 1:
            return True
    return False